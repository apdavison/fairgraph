"""
Metadata for electrophysiology experiments.

The following methods are currently supported:
    - patch clamp recording in brain slices
    - sharp electrode intracellular recording in brain slices

Coming soon:
    - patch clamp recordings in cultured neurons
    - extracellular electrode recording, including tetrodes and multi-electrode arrays

"""

# Copyright 2018-2019 CNRS

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sys
import inspect
try:
    basestring
except NameError:
    basestring = str
from datetime import datetime

from .base import KGObject, KGProxy, KGQuery, cache, lookup, build_kg_object, Field, Distribution
from .commons import QuantitativeValue, BrainRegion, CellType, StimulusType
from .core import Subject, Person
from .minds import Dataset
from .utility import compact_uri, standard_context, as_list


DEFAULT_NAMESPACE = "neuralactivity"


class Trace(KGObject):
    """Single time series recorded during an experiment or simulation.

    :class:`Trace` represents a single recording from a single channel.
    If you have a file containing recordings from multiple channels, or multiple
    recordings from a single channel, use :class:`MultiChannelMultiTrialRecording`.
    """
    namespace = DEFAULT_NAMESPACE
    _path = "/electrophysiology/trace/v0.1.0"
    # v1.0.0 now exists - check differences
    type = ["prov:Entity", "nsg:Trace"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "providerId": "nsg:providerId",
        "description": "schema:description",
        "channel": "nsg:channel",
        "channelName": "nsg:channelName",
        "projectName": "nsg:projectName",
        "dataUnit": "nsg:dataUnit",
        "timeStep": "nsg:timeStep",
        "value": "schema:value",
        "unitText": "schema:unitText",
        "unitCode": "schema:unitCode",
        "qualifiedGeneration": "prov:qualifiedGeneration",
        "wasGeneratedBy": "prov:wasGeneratedBy",
        "distribution": {
            "@id": "schema:distribution",
            "@type": "@id"},
        "downloadURL": {
            "@id": "schema:downloadURL",
            "@type": "@id"},
        "mediaType": {
            "@id": "schema:mediaType"
        },
        "minds": "https://schema.hbp.eu/",
        "partOf": "nsg:partOf"  # todo: add to nsg
    }
    fields = (
        Field("name", basestring, "name", required=True),
        Field("data_location", Distribution, "distribution", required=True),
        Field("generated_by", "electrophysiology.PatchClampExperiment", "wasGeneratedBy",
              required=True),
        Field("generation_metadata", "electrophysiology.QualifiedTraceGeneration",
              "qualifiedGeneration", required=True),
        Field("channel", int, "channel", required=True),
        # add type for units, to allow checking?
        Field("data_unit", basestring, "dataUnit", required=True),
        Field("time_step", QuantitativeValue, "timeStep", required=True),
        Field("part_of", Dataset, "partOf")
    )

    def __init__(self, name, data_location, generated_by, generation_metadata, channel, data_unit,
                 time_step, part_of=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client, use_cache=True, resolved=False):
        return super(Trace, cls).from_kg_instance(instance, client, use_cache=use_cache)

    def _build_data(self, client):
        """docstring"""
        data = super(Trace, self)._build_data(client)
        if self.time_step:
            # not sure why we're using the _alt version here
            data["timeStep"] = self.time_step.to_jsonld_alt()
        return data


class MultiChannelMultiTrialRecording(Trace):
    """Multiple time series recorded during an experiment or simulation.

    Time series may be recorded from multiple ch
    If you have a file containing only a single recording from a single channel,
    you may instead use :class:`Trace`."""
    namespace = DEFAULT_NAMESPACE
    _path = "/electrophysiology/multitrace/v0.1.0"  # for nexus
    # path = DEFAULT_NAMESPACE + "/electrophysiology/multitrace/v0.3.0"  # for nexus-int
    type = ["prov:Entity", "nsg:MultiChannelMultiTrialRecording"]
    fields = (
        Field("name", basestring, "name", required=True),
        Field("data_location", Distribution, "distribution", required=True),
        Field("generated_by",
              ("electrophysiology.PatchClampExperiment",
               "electrophysiology.ExtracellularElectrodeExperiment"),
              "wasGeneratedBy", required=True),
        Field("generation_metadata",
              "electrophysiology.QualifiedMultiTraceGeneration",
              "qualifiedGeneration",
              required=True),
        Field("channel_names", basestring, "channelName", required=True, multiple=True),
        Field("data_unit", basestring, "dataUnit", required=True,
              multiple=True),  # add type for units, to allow checking?
        Field("time_step", QuantitativeValue, "timeStep", required=True),
        Field("part_of", Dataset, "partOf")
    )

    def __init__(self, name, data_location, generated_by, generation_metadata, channel_names, data_unit,
                 time_step, part_of=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class PatchedCell(KGObject):
    """A cell recorded in patch clamp."""
    namespace = DEFAULT_NAMESPACE
    _path = "/experiment/patchedcell/v0.1.0"  # latest 0.2.1
    type = ["nsg:PatchedCell", "prov:Entity"]
    query_id = "fgModified"
    query_id_resolved = "fgResolvedModified"
    collection_class = "PatchedCellCollection"
    experiment_class = "PatchClampExperiment"
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "label": "rdfs:label",
        "brainLocation": "nsg:brainLocation",
        "brainRegion": "nsg:brainRegion",
        "eType": "nsg:eType",
        "labelingCompound": "nsg:labelingCompound"
    }
    fields = (
        Field("name", basestring, "name", required=True),
        Field("brain_location", BrainRegion, "brainRegion", required=True, multiple=True),
        Field("collection", "electrophysiology.PatchedCellCollection", "^prov:hadMember",
              reverse="cells"),
        Field("cell_type", CellType, "eType", required=False),
        Field("experiments", "electrophysiology.PatchClampExperiment",
              "^prov:used", reverse="recorded_cell", multiple=True),
        Field("pipette_id", (basestring, int), "nsg:pipetteNumber"),
        #Field("seal_resistance", QuantitativeValue.with_dimensions("electrical resistance"), "nsg:sealResistance"),
        Field("seal_resistance", QuantitativeValue, "nsg:sealResistance"),
        Field("pipette_resistance", QuantitativeValue, "nsg:pipetteResistance"),
        Field("liquid_junction_potential", QuantitativeValue, "nsg:liquidJunctionPotential"),
        Field("labeling_compound", basestring, "nsg:labelingCompound"),
        Field("reversal_potential_cl", QuantitativeValue, "nsg:chlorideReversalPotential")
    )

    def __init__(self, name, brain_location, collection=None, cell_type=None, experiments=None,
                 pipette_id=None, seal_resistance=None, pipette_resistance=None,
                 liquid_junction_potential=None, labeling_compound=None,
                 reversal_potential_cl=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)

    @classmethod
    def list(cls, client, size=100, from_index=0, api="query",
             scope="released", resolved=False, **filters):
        """List all objects of this type in the Knowledge Graph"""
        if api == "nexus":
            context = {
                'nsg': 'https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/',
                'prov': 'http://www.w3.org/ns/prov#'
            }
            filter_queries = []
            for name, value in filters.items():
                if name == "species":
                    filter_queries.append({
                        #        collection      / patchedslice / slice              / subject             / species
                        'path': '^prov:hadMember / ^nsg:hasPart / prov:wasRevisionOf / prov:wasDerivedFrom / nsg:species',
                        'op': 'eq',
                        'value': value.iri
                    })
                elif name in ("brain_region", "brain_location"):
                    filter_queries.append({
                        "path": "nsg:brainLocation / nsg:brainRegion",
                        "op": "eq",
                        "value": value.iri
                    })
                elif name == "cell_type":
                    filter_queries.append({
                        'path': 'nsg:eType',
                        'op': 'eq',
                        'value': value.iri
                    })
                elif name == "experimenter":
                    filter_queries.append({
                        #        collection      / patchedslice / patchclampactivity / person
                        'path': '^prov:hadMember / ^nsg:hasPart / ^prov:generated / prov:wasAssociatedWith',
                        'op': 'eq',
                        'value': value.id
                    })
                elif name == "lab":
                    filter_queries.append({
                        #        collection      / patchedslice / patchclampactivity / person              / organization
                        'path': '^prov:hadMember / ^nsg:hasPart / ^prov:generated / prov:wasAssociatedWith / schema:affiliation',
                        'op': 'eq',
                        'value': value.id
                    })
                else:
                    raise Exception("The only supported filters are by species, brain region, cell type "
                                    "experimenter or lab. You specified {name}".format(name=name))
            if len(filter_queries) == 0:
                return client.list(cls, api="nexus", size=size)
            elif len(filter_queries) == 1:
                filter_query = filter_queries[0]
            else:
                filter_query = {
                    "op": "and",
                    "value": filter_queries
                }
            filter_query = {"nexus": filter_query}
            return KGQuery(cls, filter_query, context).resolve(client, api="nexus", size=size)
        elif api == "query":
            return super(PatchedCell, cls).list(client, size, from_index, api,
                                                scope, resolved, **filters)
        else:
            raise ValueError("'api' must be either 'nexus' or 'query'")

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client, use_cache=True, resolved=False):
        # leaving the following, commented-out code until I check
        # that using "eq" rather than "in" for the collection filter
        # doesn't break anything.

        # D = instance.data
        # for otype in cls.type:
        #     assert otype in D["@type"]

        # # get the collection of which the cell is a part
        # prov_context = {"prov": "http://www.w3.org/ns/prov#"}
        # collection_filter = {
        #     "path": "prov:hadMember",
        #     "op": "in",
        #     "value": [instance.data["@id"]]
        # }

        # # get any experiments performed on the cell
        # expt_filter = {
        #     "path": "prov:used",
        #     "op": "eq",
        #     "value": [instance.data["@id"]]
        # }

        # obj1 = cls(D["name"],
        #            build_kg_object(BrainRegion, D["brainLocation"]["brainRegion"]),
        #            KGQuery(cls.collection_class, collection_filter, prov_context),
        #            CellType.from_jsonld(D.get("eType", None)),
        #            KGQuery(cls.experiment_class, expt_filter, prov_context),
        #            pipette_id=D.get("nsg:pipetteNumber", None),
        #            seal_resistance=QuantitativeValue.from_jsonld(D.get("nsg:sealResistance", None)),
        #            pipette_resistance=QuantitativeValue.from_jsonld(D.get("nsg:pipetteResistance", None)),
        #            liquid_junction_potential=QuantitativeValue.from_jsonld(D.get("nsg:liquidJunctionPotential", None)),
        #            labeling_compound=D.get("nsg:labelingCompound", None),
        #            reversal_potential_cl=QuantitativeValue.from_jsonld(D.get("nsg:chlorideReversalPotential", None)),
        #            id=D["@id"], instance=instance)

        D = instance.data
        if resolved:
            D = cls._fix_keys(D)

        for otype in as_list(cls.type):
            if otype not in D["@type"]:
                # todo: profile - move compaction outside loop?
                compacted_types = compact_uri(D["@type"], standard_context)
                if otype not in compacted_types:
                    print("Warning: type mismatch {} - {}".format(otype, compacted_types))
        args = {}
        for field in cls.fields:
            if field.name == "brain_location":
                if "brainRegion" in D:  # with api='query'
                    data_item = D["brainRegion"]
                else:  # with api='nexus'
                    if "brainRegion" in D["brainLocation"]:
                        data_item = D["brainLocation"]["brainRegion"]
                    else:
                        data_item = D["brainLocation"]
            elif field.intrinsic:
                data_item = D.get(field.path)
            else:
                data_item = D["@id"]
            args[field.name] = field.deserialize(data_item, client)
        obj = cls(id=D["@id"], instance=instance, **args)

        return obj

    def _build_data(self, client):
        """docstring"""
        data = super(PatchedCell, self)._build_data(client)
        data["brainLocation"] = {"brainRegion": data.pop("brainRegion")}
        return data


class Slice(KGObject):  # should move to "core" module?
    """A brain slice."""
    namespace = DEFAULT_NAMESPACE
    _path = "/core/slice/v0.1.0"
    type = ["nsg:Slice", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "name": "schema:name",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "providerId": "nsg:providerId",
        "wasDerivedFrom": "prov:wasDerivedFrom"
    }
    fields = (
        Field("name", basestring, "name", required=True),
        Field("subject", Subject, "wasDerivedFrom", required=True),
        Field("brain_slicing_activity", "electrophysiology.BrainSlicingActivity",
              "^prov:generated", reverse="slices")
    )

    def resolve(self, client, api="query"):
        if hasattr(self.subject, "resolve"):
            self.subject = self.subject.resolve(client, api=api)
        if hasattr(self.brain_slicing_activity, "resolve"):
            self.brain_slicing_activity = self.brain_slicing_activity.resolve(client, api=api)


class BrainSlicingActivity(KGObject):
    """The activity of cutting brain tissue into slices."""
    namespace = DEFAULT_NAMESPACE
    _path = "/experiment/brainslicing/v0.1.0"
    type = ["nsg:BrainSlicing", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "generated": "prov:generated",
        "used": "prov:used",
        "startedAtTime": "prov:startedAtTime",
        "label": "rdfs:label",
        "value": "schema:value",
        "unitCode": "schema:unitCode",
        "brainLocation": "nsg:brainLocation",
        "brainRegion": "nsg:brainRegion",
        "slicingPlane": "nsg:slicingPlane",
        "solution": "nsg:solution",
        "slicingAngle": "nsg:slicingAngle",
        "cuttingThickness": "nsg:cuttingThickness"
    }
    fields = (
        Field("subject", Subject, "used", required=True),
        Field("slices", Slice, "generated", multiple=True, required=True),
        Field("brain_location", BrainRegion, "brainRegion", required=False, multiple=True),
        Field("slicing_plane", basestring, "slicingPlane", required=False),
        Field("slicing_angle", float, "slicingAngle", required=False),
        Field("cutting_solution", basestring, "solution", required=False),
        Field("cutting_thickness", QuantitativeValue, "cuttingThickness", required=False),
        Field("start_time", datetime, "startedAtTime", required=False),
        Field("people", Person, "wasAssociatedWith", multiple=True, required=False)
    )
    existence_query_fields = ("subject",)  # can only slice a brain once...

    def __init__(self, subject, slices, brain_location=None, slicing_plane=None, slicing_angle=None,
                 cutting_solution=None, cutting_thickness=None, start_time=None, people=None,
                 id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client, resolved=False):
        D = instance.data
        if resolved:
            D = cls._fix_keys(D)
        for otype in as_list(cls.type):
            if otype not in D["@type"]:
                # todo: profile - move compaction outside loop?
                compacted_types = compact_uri(D["@type"], standard_context)
                if otype not in compacted_types:
                    print("Warning: type mismatch {} - {}".format(otype, compacted_types))
        args = {}
        for field in cls.fields:
            if field.name == "brain_location":
                data_item = D.get("brainLocation", {}).get("brainRegion")
            elif field.intrinsic:
                data_item = D.get(field.path)
            else:
                data_item = D["@id"]
            args[field.name] = field.deserialize(data_item, client)
        obj = cls(id=D["@id"], instance=instance, **args)
        return obj

    def _build_data(self, client):
        """docstring"""
        data = super(BrainSlicingActivity, self)._build_data(client)
        if "brainRegion" in data:
            data["brainLocation"] = {"brainRegion": data.pop("brainRegion")}
        return data

    def resolve(self, client, api="query"):
        if hasattr(self.subject, "resolve"):
            self.subject = self.subject.resolve(client, api=api)
        for i, slice in enumerate(self.slices):
            if hasattr(slice, "resolve"):
                self.slices[i] = slice.resolve(client, api=api)
        for i, person in enumerate(self.people):
            if hasattr(person, "resolve"):
                self.people[i] = person.resolve(client, api=api)


class PatchedSlice(KGObject):
    """A slice that has been recorded from using patch clamp."""
    namespace = DEFAULT_NAMESPACE
    _path = "/experiment/patchedslice/v0.1.0"
    type = ["nsg:PatchedSlice", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "dcterms": "http://purl.org/dc/terms/",
        "name": "schema:name",
        "brainRegion": "nsg:BrainRegion",
        "hasPart": "nsg:hasPart",
        "wasRevisionOf": "prov:wasRevisionOf"
    }
    #collection_class = "PatchedCellCollection"
    #recording_activity_class = "PatchClampActivity"
    fields = (
        Field("name", basestring, "name", required=True),
        Field("slice", Slice, "wasRevisionOf", required=True),
        Field("recorded_cells", "electrophysiology.PatchedCellCollection", "hasPart",
              required=True),
        Field("recording_activity", "electrophysiology.PatchClampActivity", "^prov:generated",
              reverse="recorded_slice")
    )

    def __init__(self, name, slice, recorded_cells, recording_activity=None,
                 id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)

    # @classmethod
    # @cache
    # def from_kg_instance(cls, instance, client):
    #     D = instance.data
    #     for otype in cls.type:
    #         assert otype in D["@type"]

    #     # filter to get recording activity
    #     recording_activity_filter = {
    #         "path": "prov:generated",
    #         "op": "in",
    #         "value": D["@id"]
    #     }
    #     context={"prov": "http://www.w3.org/ns/prov#"}

    #     return cls(D["name"],
    #                slice=KGProxy(Slice, D["wasRevisionOf"]["@id"]),
    #                recorded_cells=KGProxy(cls.collection_class, D["hasPart"]["@id"]),
    #                recording_activity=KGQuery(cls.recording_activity_class, recording_activity_filter, context),
    #                id=D["@id"],
    #                instance=instance)


class PatchedCellCollection(KGObject):
    """A collection of patched cells."""
    namespace = DEFAULT_NAMESPACE
    _path = "/experiment/patchedcellcollection/v0.1.0"
    type = ["nsg:Collection"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "size": "schema:size",
        "hadMember": "prov:hadMember"
    }
    #member_class = "PatchedCell"
    #recorded_from_class = "PatchedSlice"
    fields = (
        Field("name", basestring, "name", required=True),
        Field("cells", PatchedCell, "hadMember", required=True),
        Field("slice", PatchedSlice, "^nsg:hasPart", reverse="recorded_cells")
    )

    def __init__(self, name, cells, slice=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)

    @property
    def size(self):
        return len(self.cells)

    # @classmethod
    # @cache
    # def from_kg_instance(cls, instance, client):
    #     """
    #     docstring
    #     """
    #     D = instance.data
    #     for otype in cls.type:
    #         assert otype in D["@type"]

    #     recorded_slice_filter={
    #         "path": "nsg:hasPart",
    #         "op": "in",
    #         "value": D["@id"]
    #     }
    #     context = {"nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/"}

    #     return cls(name=D["name"],
    #                slice=KGQuery(cls.recorded_from_class, recorded_slice_filter, context),
    #                cells=[KGProxy(cls.member_class, member_uri["@id"])
    #                       for member_uri in D["hadMember"]],
    #                id=D["@id"],
    #                instance=instance)

    # def _build_data(self, client):
    #     """docstring"""
    #     data = {}
    #     data["name"] = self.name
    #     data["hadMember"] = [{
    #         "@type": lookup(self.member_class).type,
    #         "@id": cell.id
    #     } for cell in self.cells]
    #     return data


class PatchClampActivity(KGObject):  # rename to "PatchClampRecording"?
    """A patch clamp recording session."""
    namespace = DEFAULT_NAMESPACE
    _path = "/experiment/wholecellpatchclamp/v0.1.0"
    type = ["nsg:WholeCellPatchClamp", "prov:Activity"]
    #generates_class = "PatchedSlice"
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "used": "prov:used",
        "generated": "prov:generated",
        "wasAssociatedWith": "prov:wasAssociatedWith"
    }
    fields = (
        Field("name", basestring, "name", required=True),
        Field("slice", Slice, "used", required=True),
        Field("recorded_slice", PatchedSlice, "generated", required=True),
        Field("protocol", basestring, "protocol"),
        Field("people", Person, "wasAssociatedWith", multiple=True)
    )

    def __init__(self, name, slice, recorded_slice, protocol=None, people=None,
                 id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)

    # todo: custom exists(), based on slice not on name


class PatchClampExperiment(KGObject):
    """
    Stimulation of the neural tissue and recording of the responses during a patch clamp
    recording session.
    """
    namespace = DEFAULT_NAMESPACE
    _path = "/electrophysiology/stimulusexperiment/v0.1.0"
    type = ["nsg:StimulusExperiment", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "label": "rdfs:label"
    }
    #recorded_cell_class = "PatchedCell"
    fields = (
        Field("name", basestring, "name", required=True),
        Field("recorded_cell", PatchedCell, "prov:used", required=True),
        Field("stimulus", StimulusType, "nsg:stimulusType", required=False),
        Field("traces", (Trace, MultiChannelMultiTrialRecording), "^prov:wasGeneratedBy",
              multiple=True, reverse="generated_by")
    )

    def __init__(self, name, recorded_cell, stimulus=None, traces=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client, resolved=False):
        """
        docstring
        """
    #     D = instance.data
    #     assert 'nsg:StimulusExperiment' in D["@type"]

    #     # get the recorded traces
    #     traces_filter = {
    #         "path": "prov:wasGeneratedBy",
    #         "op": "eq",
    #         "value": D["@id"]
    #     }
    #     context = {"prov": "http://www.w3.org/ns/prov#"}

    #     return cls(name=D["name"], #name=D["schema:name"],
    #                #recorded_cell=KGProxy(cls.recorded_cell_class, D["prov:used"][0]["@id"]),
    #                recorded_cell=KGProxy(cls.recorded_cell_class, D["prov:used"]["@id"]),
    #                stimulus=D["nsg:stimulus"],
    #                traces=KGQuery(Trace, traces_filter, context),
    #                id=D["@id"],
    #                instance=instance)
        D = instance.data
        if resolved:
            D = cls._fix_keys(D)

        for otype in as_list(cls.type):
            if otype not in D["@type"]:
                # todo: profile - move compaction outside loop?
                compacted_types = compact_uri(D["@type"], standard_context)
                if otype not in compacted_types:
                    print("Warning: type mismatch {} - {}".format(otype, compacted_types))
        args = {}
        for field in cls.fields:
            if field.name == "stimulus":
                if "nsg:stimulus" in D:
                    data_item = D["nsg:stimulus"]["nsg:stimulusType"]
                elif "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/stimulusType" in D:
                    data_item = D["https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/stimulusType"]
                else:
                    data_item = None
            elif field.intrinsic:
                data_item = D.get(field.path)
            else:
                data_item = D["@id"]
            args[field.name] = field.deserialize(data_item, client)
        obj = cls(id=D["@id"], instance=instance, **args)
        return obj

    def _build_data(self, client):
        """docstring"""
        data = super(PatchClampExperiment, self)._build_data(client)
        data["nsg:stimulus"] = {"nsg:stimulusType": data.pop("nsg:stimulusType", None)}
        return data

    @classmethod
    def list(cls, client, size=100, from_index=0, api="query",
             scope="released", resolved=False, **filters):
        """List all objects of this type in the Knowledge Graph"""
        # we need to add the additional filter below, as PatchClampExperiment and
        # IntraCellularSharpElectrodeExperiment share the same path
        # and JSON-LD type ("nsg:StimulusExperiment")
        if api == "nexus":
            filter = {'path': 'prov:used / rdf:type', 'op': 'eq', 'value': 'nsg:PatchedCell'}
            context = {
                "nsg": cls.context["nsg"],
                "prov": cls.context["prov"],
                "rdf": 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
            }
            return client.list(cls, size=size, api=api, filter=filter, context=context)
        elif api == "query":
            # todo: what about filtering if api="query"
            return super(PatchClampExperiment, cls).list(client, size, from_index, api,
                                                         scope, resolved, **filters)
        else:
            raise ValueError("'api' must be either 'nexus' or 'query'")

    @property
    def dataset(self):
        context = {
            "nsg": self.context["nsg"],
            "prov": self.context["prov"]
        }
        filter = {
            "nexus": {
                "path": "^nsg:partOf / prov:wasGeneratedBy",
                "op": "eq",
                "value": self.id
            }
        }
        return KGQuery(Dataset, filter, context)


class QualifiedTraceGeneration(KGObject):
    """Additional information about the generation of a single-channel electrophysiology trace."""
    namespace = DEFAULT_NAMESPACE
    _path = "/electrophysiology/tracegeneration/v0.1.0"
    type = ["prov:Generation", "nsg:TraceGeneration"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "sweep": "nsg:sweep",
        "activity": "prov:activity",
        "label": "rdfs:label",
        "value": "schema:value",
        "unitCode": "schema:unitCode",
        "targetHoldingPotential": "nsg:targetHoldingPotential"
    }
    fields = (
        Field("name", basestring, "name", required=True),
        Field("stimulus_experiment",
              (PatchClampExperiment, "electrophysiology.IntraCellularSharpElectrodeExperiment"),
              "activity", required=True),
        Field("sweep", int, "sweep", multiple=True, required=True),
        #Field("traces", (Trace, MultiChannelMultiTrialRecording), "^foo"),
        Field("holding_potential", QuantitativeValue, "targetHoldingPotential")
    )

    def __init__(self, name, stimulus_experiment, sweep, #traces=None,
                 holding_potential=None,
                 id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class ImplantedBrainTissue(KGObject):
    """docstring"""
    namespace = DEFAULT_NAMESPACE
    _path = "/core/implantedbraintissue/v0.1.0"
    type = ["nsg:ImplantedBrainTissue", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "name": "schema:name",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "providerId": "nsg:providerId",
        "wasDerivedFrom": "prov:wasDerivedFrom"
    }
    fields = (
        Field("name", basestring, "name", required=True),
        Field("subject", Subject, "wasDerivedFrom", required=True)
    )

    def resolve(self, client):
        if hasattr(self.subject, "resolve"):
            self.subject = self.subject.resolve(client)


class ElectrodeImplantationActivity(KGObject):
    """docstring"""
    namespace = DEFAULT_NAMESPACE
    _path = "/experiment/electrodeimplantation/v0.1.5"
    type = ["nsg:ElectrodeImplantation", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "generated": "prov:generated",
        "brainLocation": "nsg:brainLocation",
        "brainRegion": "nsg:brainRegion",
        "used": "prov:used",
        "startedAtTime": "prov:startedAtTime",
        "endAtTime": "prov:endedAtTime",
        "label": "rdfs:label",
        "value": "schema:value",
        "unitCode": "schema:unitCode",
        "anesthesia": "nsg:anesthesia"
    }
    fields = (
        Field("subject", Subject, "used", required=True),
        Field("implanted_brain_tissues", ImplantedBrainTissue, "generated",
              multiple=True, required=True),
        Field("brain_location", BrainRegion, "brainRegion", required=False, multiple=True),
        Field("start_time", datetime, "startedAtTime", required=False),
        Field("end_time", datetime, "endedAtTime", required=False),
        Field("people", Person, "wasAssociatedWith", multiple=True, required=False)
    )
    existence_query_fields = ("subject")

    def __init__(self, subject, implanted_brain_tissues, brain_location,
                 start_time=None, end_time=None, people=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client, resolved=False):
        D = instance.data
        for otype in as_list(cls.type):
            if otype not in D["@type"]:
                # todo: profile - move compaction outside loop?
                compacted_types = compact_uri(D["@type"], standard_context)
                if otype not in compacted_types:
                    print("Warning: type mismatch {} - {}".format(otype, compacted_types))
        args = {}
        for field in cls.fields:
            if field.name == "brain_location":
                data_item = D.get("brainLocation", {}).get("brainRegion")
            elif field.intrinsic:
                data_item = D.get(field.path)
            else:
                data_item = D["@id"]
            args[field.name] = field.deserialize(data_item, client)
        obj = cls(id=D["@id"], instance=instance, **args)
        return obj

    def _build_data(self, client):
        """docstring"""
        data = super(ElectrodeImplantationActivity, self)._build_data(client)
        if "brainRegion" in data:
            data["brainLocation"] = {"brainRegion": data.pop("brainRegion")}
        return data

    def resolve(self, client):
        if hasattr(self.subject, "resolve"):
            self.subject = self.subject.resolve(client)
        for i, slice in enumerate(self.slices):
            if hasattr(self.implanted_brain_tissues, "resolve"):
                self.implanted_brain_tissues[i] = self.implanted_brain_tissues.resolve(client)
        for i, person in enumerate(self.people):
            if hasattr(person, "resolve"):
                self.people[i] = person.resolve(client)


class ExtracellularElectrodeExperiment(PatchClampExperiment):
    """docstring"""
    namespace = DEFAULT_NAMESPACE
    _path = "/electrophysiology/stimulusexperiment/v0.1.4"
    type = ["nsg:StimulusExperiment", "prov:Activity"]
    recorded_cell_class = "ImplantedBrainTissue"
    fields = (
        Field("name", basestring, "name", required=True),
        Field("recorded_cell", ImplantedBrainTissue, "prov:used", required=True),
        Field("stimulus", StimulusType, "nsg:stimulusType", required=True),
        Field("traces", (Trace, MultiChannelMultiTrialRecording), "^prov:wasGeneratedBy",
              multiple=True)
    )

    @classmethod
    def list(cls, client, size=100, api='nexus', **filters):
        """List all objects of this type in the Knowledge Graph"""
        filter = {'path': 'prov:used / rdf:type',
                  'op': 'eq',
                  'value': "nsg:ImplantedBrainTissue"}
        context = {
            "nsg": cls.context["nsg"],
            "prov": cls.context["prov"],
            "rdf": 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
        }
        # todo: what about filtering if api="query"
        return client.list(cls, size=size, api=api, filter=filter, context=context)


class IntraCellularSharpElectrodeRecordedCell(PatchedCell):
    """A cell recorded intracellularly with a sharp electrode."""
    namespace = DEFAULT_NAMESPACE
    _path = "/experiment/intrasharprecordedcell/v0.1.0"
    type = ["nsg:IntraCellularSharpElectrodeRecordedCell", "prov:Entity"]
    collection_class = "IntraCellularSharpElectrodeRecordedCellCollection"
    experiment_class = "IntraCellularSharpElectrodeExperiment"
    fields = (
        Field("name", basestring, "name", required=True),
        Field("brain_location", BrainRegion, "brainRegion", required=True, multiple=True),
        Field("collection", "electrophysiology.IntraCellularSharpElectrodeRecordedCellCollection",
              "^prov:hadMember", reverse="cells"),
        Field("cell_type", CellType, "eType", required=False),
        Field("experiments", "electrophysiology.IntraCellularSharpElectrodeExperiment",
              "^prov:used", multiple=True, reverse="recorded_cell"),
        Field("pipette_id", (basestring, int), "nsg:pipetteNumber"),
        #Field("seal_resistance", QuantitativeValue.with_dimensions("electrical resistance"), "nsg:sealResistance"),
        Field("seal_resistance", QuantitativeValue, "nsg:sealResistance"),
        Field("pipette_resistance", QuantitativeValue, "nsg:pipetteResistance"),
        Field("liquid_junction_potential", QuantitativeValue, "nsg:liquidJunctionPotential"),
        Field("labeling_compound", basestring, "nsg:labelingCompound"),
        Field("reversal_potential_cl", QuantitativeValue, "nsg:chlorideReversalPotential")
    )


class IntraCellularSharpElectrodeRecording(PatchClampActivity):
    """A sharp-electrode recording session."""
    namespace = DEFAULT_NAMESPACE
    _path = "/experiment/intrasharpelectrode/v0.1.0"
    type = ["nsg:IntraCellularSharpElectrode", "prov:Activity"]
    generates_class = "IntraCellularSharpElectrodeRecordedSlice"
    fields = (
        Field("name", basestring, "name", required=True),
        Field("slice", Slice, "used", required=True),
        Field("recorded_slice", "electrophysiology.IntraCellularSharpElectrodeRecordedSlice",
              "generated", required=True),
        Field("protocol", basestring, "protocol"),
        Field("people", Person, "wasAssociatedWith")
    )


class IntraCellularSharpElectrodeRecordedCellCollection(PatchedCellCollection):
    """A collection of cells recorded with a sharp electrode."""
    namespace = DEFAULT_NAMESPACE
    _path = "/experiment/intrasharprecordedcellcollection/v0.1.0"
    type = ["nsg:Collection"]
    member_class = "IntraCellularSharpElectrodeRecordedCell"
    recorded_from_class = "IntraCellularSharpElectrodeRecordedSlice"
    fields = (
        Field("name", basestring, "name", required=True),
        Field("cells", IntraCellularSharpElectrodeRecordedCell, "hadMember", required=True),
        Field("slice", "electrophysiology.IntraCellularSharpElectrodeRecordedSlice",
              "^nsg:hasPart", reverse="recorded_cells")
    )


class IntraCellularSharpElectrodeRecordedSlice(PatchedSlice):
    """A slice that has been recorded from using a sharp electrode."""
    namespace = DEFAULT_NAMESPACE
    _path = "/experiment/intrasharprecordedslice/v0.1.0"
    type = ["nsg:IntraCellularSharpElectrodeRecordedSlice", "prov:Entity"]
    collection_class = "IntraCellularSharpElectrodeRecordedCellCollection"
    recording_activity_class = "IntraCellularSharpElectrodeRecording"
    fields = (
        Field("name", basestring, "name", required=True),
        Field("slice", Slice, "wasRevisionOf", required=True),
        Field("recorded_cells", IntraCellularSharpElectrodeRecordedCellCollection, "hasPart",
              required=True),
        Field("recording_activity", IntraCellularSharpElectrodeRecording, "^prov:generated",
              reverse="recorded_slice")
    )


class IntraCellularSharpElectrodeExperiment(PatchClampExperiment):
    """
    Stimulation of the neural tissue and recording of the responses with
    a sharp intracellular electrode.
    """
    namespace = DEFAULT_NAMESPACE
    _path = "/electrophysiology/stimulusexperiment/v0.2.1"
    type = ["nsg:StimulusExperiment", "prov:Activity"]
    recorded_cell_class = "IntraCellularSharpElectrodeRecordedCell"
    fields = (
        Field("name", basestring, "name", required=True),
        Field("recorded_cell", IntraCellularSharpElectrodeRecordedCell, "prov:used",
              required=True),
        Field("stimulus", StimulusType, "nsg:stimulusType", required=True),
        Field("traces", Trace, "^prov:wasGeneratedBy", multiple=True, reverse="generated_by"),
    )

    @classmethod
    def list(cls, client, size=100, from_index=0, api="query",
             scope="released", resolved=False, **filters):
        """List all objects of this type in the Knowledge Graph"""
        if api == "nexus":
            # we need to add an additional filter, as PatchClampExperiment and
            # IntraCellularSharpElectrodeExperiment share the same path
            # and JSON-LD type ("nsg:StimulusExperiment")
            filter = {'path': 'prov:used / rdf:type',
                      'op': 'eq',
                      'value': "nsg:IntraCellularSharpElectrodeRecordedCell"}
            context = {
                "nsg": cls.context["nsg"],
                "prov": cls.context["prov"],
                "rdf": 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
            }
            return client.list(cls, size=size, from_index=from_index, api=api, scope=scope,
                               resolved=resolved, filter=filter, context=context)
        elif api == "query":
            # todo: what about filtering?
            return super(IntraCellularSharpElectrodeExperiment, cls).list(
                client, size, from_index, api, scope, resolved, **filters)


class QualifiedMultiTraceGeneration(KGObject):
    namespace = DEFAULT_NAMESPACE
    _path = "/electrophysiology/multitracegeneration/v0.1.0" # for nexus
    #path = DEFAULT_NAMESPACE + "/electrophysiology/multitracegeneration/v0.2.0"  # for nexus-int
    type = ["prov:Generation", "nsg:MultiTraceGeneration"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "sweep": "nsg:sweep",
        "activity": "prov:activity",
        "label": "rdfs:label",
        "value": "schema:value",
        "unitCode": "schema:unitCode",
        "targetHoldingPotential": "nsg:targetHoldingPotential"
    }

    fields = (
        Field("name", basestring, "name", required=True),
        Field("stimulus_experiment",
              (ExtracellularElectrodeExperiment,
               IntraCellularSharpElectrodeExperiment,
               PatchClampExperiment),
              "activity",
              required=True),
        Field("sweeps", int, "sweep", multiple=True, required=True),
        #Field("traces", (Trace, MultiChannelMultiTrialRecording), "^foo"),
        Field("holding_potential", QuantitativeValue, "targetHoldingPotential")
    )


    def __init__(self, name, stimulus_experiment, sweeps, #traces=None,
                 holding_potential=None,
                 id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
            if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__ == __name__]


def use_namespace(namespace):
    """Set the namespace for all classes in this module."""
    for cls in list_kg_classes():
        cls.namespace = namespace
