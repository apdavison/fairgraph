# coding: utf-8

"""
Corresponds to "Accessing model information from the Knowledge Graph in a Jupyter notebook"
"""

import os
import pandas as pd

from fairgraph import KGClient
from fairgraph.brainsimulation import ModelProject, MEModel
from fairgraph.commons import Species, CellType, BrainRegion, AbstractionLevel, ModelScope
from fairgraph.base import as_list

import pytest


token = os.environ.get("HBP_AUTH_TOKEN", None)
if token:
    client = KGClient(token, nexus_endpoint="https://nexus.humanbrainproject.org/v0")


@pytest.mark.skip("comment this out to run the test")
@pytest.mark.skipif(token is None,
                    reason="No token provided. Please set environment variable HBP_AUTH_TOKEN")
def test_all():
    ModelProject.set_strict_mode(False)  # check: will this interfere with other tests?
    MEModel.set_strict_mode(False)

    ## Get a list of possible filter terms

    for cls in (Species, CellType, BrainRegion, AbstractionLevel, ModelScope):
        print("\nPossible values of {}:\n  - ".format(cls.__name__))
        print("\n  - ".join(cls.iri_map.keys()))

    ## Find models of hippocampus pyramidal neurons

    models = ModelProject.list(client,
                            brain_region="hippocampus",
                            model_of="single cell",
                            species="Rattus norvegicus")
    len(models)
    columns = ("name", "brain_region", "celltype", "authors")

    data = []
    for model in models:
        row = {}
        for attr in columns:
            value = getattr(model, attr)
            if hasattr(value, "label"):
                row[attr] = value.label
            elif attr == "authors":
                row[attr] = ", ".join("{au.given_name} {au.family_name}".format(au=obj.resolve(client))
                                    for obj in as_list(value))
            else:
                row[attr] = value
        data.append(row)

    df = pd.DataFrame(data=data, columns=columns)  #.sort_values(by=['name'], kind="mergesort")
    dfStyler = df.style.set_properties(**{'text-align': 'left'})
    dfStyler.set_table_styles([dict(selector='th', props=[('text-align', 'left')])])


    # Exploring a single model

    # take the last model from the list above, and show its versions
    example_model = models[-1]
    example_model.instances

    # take the last version (not necessarily the most recent)
    instance = as_list(example_model.instances)[-1].resolve(client)
    instance
    instance.timestamp.isoformat()

    code = instance.main_script.resolve(client)
    code.code_format
    code.code_location

    morph = instance.morphology.resolve(client)
    morph.morphology_file

    def print_model_information(index):
        model = models[index]
        instance = as_list(model.instances)[-1].resolve(client)
        code = instance.main_script.resolve(client)
        morph = instance.morphology.resolve(client)
        print(instance.name, instance.timestamp.isoformat())
        print(code.code_location)
        print(morph.morphology_file)

    print_model_information(99)

    # not all models have morphologies, I'm not sure if this is expected or not.
    # Here is a list of models with morphologies
    for model in models:
        for instance in as_list(model.instances):
            instance = instance.resolve(client)
            morph_file = instance.morphology.resolve(client).morphology_file
            if morph_file:
                print(instance.name, morph_file)
