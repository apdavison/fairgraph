
# coding: utf-8

"""
Corresponds to "Accessing neural activity data in a Jupyter notebook"
"""

import os
from pprint import pprint
from io import BytesIO

import requests
import numpy as np
import matplotlib.pyplot as plt

from fairgraph.commons import BrainRegion, Species, CellType
from fairgraph.electrophysiology import PatchedCell, Trace
from fairgraph import KGClient
from fairgraph.base import KGQuery
from fairgraph.minds import Dataset

import pytest


token = os.environ.get("HBP_AUTH_TOKEN", None)

if token:
    client = KGClient(token, nexus_endpoint="https://nexus.humanbrainproject.org/v0")


@pytest.mark.skip("comment this out to run the test")
@pytest.mark.skipif(token is None,
                    reason="No token provided. Please set environment variable HBP_AUTH_TOKEN")
def test_all():
    ## Search based on brain region

    cells_in_ca1 = PatchedCell.list(client, brain_region=BrainRegion("hippocampus CA1"))
    pprint([cell.brain_location for cell in cells_in_ca1])

    ### Download the recorded data for one of these cells

    example_cell = cells_in_ca1[3]
    experiment = example_cell.experiments.resolve(client)
    trace = experiment.traces.resolve(client)
    print(trace.time_step)
    print(trace.data_unit)

    download_url = trace.data_location.location
    print(download_url)

    data = np.genfromtxt(BytesIO(requests.get(download_url).content))

    ### Plot the data

    times = data[:, 0]
    signals = data[:, 1:]

    # plot the first 100 signals
    plt.figure(figsize=(18, 16), dpi= 80, facecolor='w', edgecolor='k')
    xlim = (times.min(), times.max())
    for i in range(1, 101):
        plt.subplot(10, 10, i)
        plt.plot(times, data[:, i], 'grey')
        plt.xlim(*xlim)
        plt.axis('off')

    ## Search based on species

    cells_from_mouse = PatchedCell.list(client, species=Species("Mus musculus"))
    for cell in cells_from_mouse[:10]:
        pprint(cell.collection.resolve(client).slice.resolve(client).slice.resolve(client).subject.resolve(client).species)

    ## Search based on cell type

    pyramidal_neurons = PatchedCell.list(client, cell_type=CellType("hippocampus CA1 pyramidal cell"))
    pprint([pn.cell_type for pn in pyramidal_neurons[:10]])

    # An activity dataset with minimal metadata

    Dataset.set_strict_mode(False)

    query = {
        "path": "minds:specimen_group / minds:subjects / minds:samples / minds:methods / schema:name",
        "op": "in",
        "value": ["Electrophysiology recording",
                "Voltage clamp recording",
                "Single electrode recording",
                "functional magnetic resonance imaging"]
    }
    context = {
                "schema": "http://schema.org/",
                "minds": "https://schema.hbp.eu/minds/"
    }

    activity_datasets = KGQuery(Dataset, query, context).resolve(client)
    for dataset in activity_datasets:
        print("* " + getattr(dataset, "name", "unknown"))

    dataset = activity_datasets[-1]
    #dataset.owners[0].resolve(client)
    #dataset.license.resolve(client)

    ## An activity dataset with extended metadata

    dataset = client.by_name(Dataset, "sIPSCs from juvenile (P21-30) C57Bl6/J male mice from CA1 pyramidal neurons receiving input from PV+ interneurons")
    query = {
        "path": "nsg:partOf",
        "op": "eq",
        "value": dataset.id
    }
    context = {
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/"
    }
    traces = KGQuery(Trace, query, context).resolve(client)
    print(traces)

    tr0 = traces[0]

    print(tr0.name)
    print(tr0.channel)
    print(tr0.time_step)
    print(tr0.data_unit)
    print(tr0.data_location)

    experiment = tr0.generated_by.resolve(client)
    print(experiment.name)

    cell = experiment.recorded_cell.resolve(client)

    print(cell.brain_location)
    print(cell.cell_type)
    print(cell.reversal_potential_cl)
