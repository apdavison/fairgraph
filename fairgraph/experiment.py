"""
Metadata for entities that are used in multiple experimental contexts (e.g. in both electrophysiology and optophysiology).

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
from .commons import QuantitativeValue, QuantitativeValueRange, BrainRegion, License, CultureType, StimulusType
from .core import Subject, Person, Protocol
from .utility import compact_uri, standard_context, as_list

DEFAULT_NAMESPACE = "neuralactivity"


class CranialWindow(KGObject):
    """A window (partially) through the skull."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/cranialwindow/v0.1.1"
    type = ["nsg:CranialWindow", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "value": "schema:value",
        "name": "schema:name",
        "brainLocation": "nsg:brainLocation",
        "brainRegion": "nsg:brainRegion",
    	"windowType":"nsg:windowType",
    	"diameter":"nsg:diameter",
    	"fluorescenceLabeling":"nsg:fluorescenceLabeling",
        "description": "schema:description",
        "minds": "https://schema.hbp.eu/"
        }
    fields = (
        Field("name", basestring, "name", required=True),
        Field("brain_location", BrainRegion, "brainRegion", multiple=True),
        Field("window_type", basestring, "windowType"),
        Field("diameter", QuantitativeValue, "diameter"),
        Field("fluorescence_labeling", basestring, "fluorescenceLabeling"),
        Field("description", basestring, "description"),
        Field("generated_by", "Craniotomy", "^prov:generated", reverse="cranial_window"),
        Field("activity", ("optophysiology.TwoPhotonImaging", "electrophysiology.ElectrodeImplantationActivity", "electrophysiology.PatchClampActivity"), "^prov:used", reverse=["target", "cranial_window", "recorded_tissue"])
    )

    def __init__(self, name, brain_location=None, window_type=None, diameter=None, fluorescence_labeling=None,
    description=None, generated_by=None, activity=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class Craniotomy(KGObject):
    """Surgical procedure to give optical access through the skull to the brain (dura)."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/craniotomy/v0.2.0"
    type = ["nsg:Craniotomy", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "generated": "prov:generated",
        "used": "prov:used",
        "anesthesia": "nsg:anesthesia",
        "startedAtTime": "prov:startedAtTime",
        "endedAtTime": "prov:endedAtTime",
        "hadProtocol": "prov:hadProtocol",
        "wasAssociatedWith": "prov:wasAssociatedWith"
    }
    fields = (
        Field("name", basestring, "name", required=True),
        Field("subject", Subject, "used", required=True),
        Field("cranial_window", CranialWindow, "generated", required=True),
        Field("anesthesia", basestring, "anesthesia"),
	    Field("protocol", Protocol, "hadProtocol"),
        Field("start_time", datetime, "startedAtTime"),
        Field("end_time", datetime, "endedAtTime"),
        Field("people", Person, "wasAssociatedWith", multiple=True)
    )

    def __init__(self, name, subject, cranial_window, anesthesia=None, protocol=None, start_time=None, end_time=None, people=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


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
        Field("provider_id", basestring, "providerId"),
        Field("brain_slicing_activity",  "electrophysiology.BrainSlicingActivity", "^prov:generated", reverse="slices"),
        #Field("activity", ("electrophysiology.PatchClampActivity", "optophysiology.TwoPhotonImaging"), "^prov:used", reverse=["recorded_tissue","target"])
        #  support for multiple reverses not implemented
        Field("activity", ("electrophysiology.PatchClampActivity", "optophysiology.TwoPhotonImaging"), "^prov:used", reverse="recorded_tissue")
    )

    def resolve(self, client, api="query", use_cache=True):
        if hasattr(self.subject, "resolve"):
            self.subject = self.subject.resolve(client, api=api, use_cache=use_cache),
        if hasattr(self.brain_slicing_activity, "resolve"):
            self.brain_slicing_activity = self.brain_slicing_activity.resolve(client, api=api, use_cache=use_cache)
        return self


class CellCulture(KGObject):  # should move to "core" module?
    """A cell culture."""
    namespace = DEFAULT_NAMESPACE
    _path = "/experiment/cellculture/v0.1.0"
    type = ["nsg:CellCulture", "prov:Entity"]
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
        Field("culturing_activity", "electrophysiology.CellCultureActivity",
              "^prov:generated", reverse="cell_culture"),
        Field("experiment", ("electrophysiology.PatchClampActivity"), "^prov:used", reverse="recorded_tissue")
    )

    def __init__(self, name, subject, culturing_activity=None, experiment=None,
                 id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


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
        "endedAtTime": "prov:endedAtTime",
        "label": "rdfs:label",
        "value": "schema:value",
        "unitCode": "schema:unitCode",
        "brainLocation": "nsg:brainLocation",
        "brainRegion": "nsg:brainRegion",
        "slicingPlane": "nsg:slicingPlane",
        "solution": "nsg:solution",
        "slicingAngle": "nsg:slicingAngle",
        "hemisphere": "nsg:hemisphere",
        "cuttingThickness": "nsg:cuttingThickness",
        "wasAssociatedWith": "prov:wasAssociatedWith"
    }
    fields = (
        Field("subject", Subject, "used", required=True),
        Field("slices", Slice, "generated", multiple=True, required=True),
        Field("brain_location", BrainRegion, "brainRegion", multiple=True),
        Field("hemisphere", basestring, "hemisphere"), # choice of Left, Right
        Field("slicing_plane", basestring, "slicingPlane"), # Sagittal, Para-sagittal, Coronal, Horizontal
        Field("slicing_angle", float, "slicingAngle"),
        Field("cutting_solution", basestring, "solution"),
        Field("cutting_thickness", (QuantitativeValueRange, QuantitativeValue), "cuttingThickness"),
        Field("start_time", datetime, "startedAtTime"),
        Field("end_time", datetime, "endedAtTime"),
        Field("people", Person, "wasAssociatedWith", multiple=True)
    )
    existence_query_fields = ("subject",)  # can only slice a brain once...

    def __init__(self, subject, slices, brain_location=None, hemisphere=None, slicing_plane=None, slicing_angle=None,
                 cutting_solution=None, cutting_thickness=None, start_time=None, end_time=None, people=None,
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

    def _build_data(self, client, all_fields=False):
        """docstring"""
        data = super(BrainSlicingActivity, self)._build_data(client, all_fields=all_fields)
        if "brainRegion" in data:
            data["brainLocation"] = {"brainRegion": data.pop("brainRegion")}
        return data

    def resolve(self, client, api="query", use_cache=True):
        if hasattr(self.subject, "resolve"):
            self.subject = self.subject.resolve(client, api=api, use_cache=use_cache)
        for i, slice in enumerate(self.slices):
            if hasattr(slice, "resolve"):
                self.slices[i] = slice.resolve(client, api=api, use_cache=use_cache)
        for i, person in enumerate(self.people):
            if hasattr(person, "resolve"):
                self.people[i] = person.resolve(client, api=api, use_cache=use_cache)
        return self


class CulturingActivity(KGObject):
    """The activity of preparing a cell culture from whole brain."""
    namespace = DEFAULT_NAMESPACE
    _path = "/experiment/culturingactivity/v0.2.0"
    type = ["nsg:CulturingActivity", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "generated": "prov:generated",
        "used": "prov:used",
        "startedAtTime": "prov:startedAtTime",
        "endedAtTime": "prov:endedAtTime",
        "label": "rdfs:label",
        "value": "schema:value",
        "brainLocation": "nsg:brainLocation",
        "brainRegion": "nsg:brainRegion",
        "hemisphere": "nsg:hemisphere",
        "age": "nsg:age",
        "solution": "nsg:solution",
        "cultureType": "nsg:cultureType"
    }
    fields = (
        Field("subject", Subject, "used", required=True),
        Field("cell_culture", CellCulture, "generated", required=True),
        Field("brain_location", BrainRegion, "brainRegion", multiple=True),
        Field("culture_type", CultureType, "cultureType"),
        Field("culture_age", QuantitativeValueRange, "age"),
        Field("hemisphere", basestring, "hemisphere"), # choice of Left, Right
        Field("culture_solution", basestring, "solution"),
        Field("start_time", datetime, "startedAtTime"),
        Field("end_time", datetime, "endedAtTime"),
        Field("people", Person, "wasAssociatedWith", multiple=True)
    )
    existence_query_fields = ("subject",)  # can only slice a brain once...

    def __init__(self, subject, cell_culture, brain_location=None, culture_type=None, culture_age=None,
                 hemisphere=None, culture_solution=None, start_time=None, end_time=None, people=None,
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

    def _build_data(self, client, all_fields=False):
        """docstring"""
        data = super(CulturingActivity, self)._build_data(client, all_fields=all_fields)
        if "brainRegion" in data:
            data["brainLocation"] = {"brainRegion": data.pop("brainRegion")}
        return data

    def resolve(self, client, api="query", use_cache=True):
        if hasattr(self.subject, "resolve"):
            self.subject = self.subject.resolve(client, api=api, use_cache=use_cache)
        for i, person in enumerate(self.people):
            if hasattr(person, "resolve"):
                self.people[i] = person.resolve(client, api=api, use_cache=use_cache)
        return self


class VisualStimulus(KGObject):
    """A generic visual stimulus."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/visualstimulus/v0.1.0"
    type = ["nsg:VisualStimulus", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "minds": "https://schema.hbp.eu/",
        "value": "schema:value",
        "name": "schema:name",
        "description": "schema:description",
        "distribution": {
            "@id": "schema:distribution",
            "@type": "@id"},
        "downloadURL": {
            "@id": "schema:downloadURL",
            "@type": "@id"},
        "mediaType": {
            "@id": "schema:mediaType"
        }
    }
    fields = (
        Field("name", basestring, "name", required=True),
        Field("description", basestring, "description"),
        Field("distribution", Distribution, "distribution"),
        Field("stimulation", "optophysiology.VisualStimulation", "^prov:used", reverse="stimulus")
    )

    def __init__(self, name, description=None, distribution=None, stimulation=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class VisualStimulation(KGObject):
    """Presentation of a visual stimulus to the subject of the experiment."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/visualstimulation/v0.1.0"
    type = ["nsg:VisualStimulation", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "used": "prov:used",
        "wasInformedBy": "nsg:wasInformedBy",
        "name": "schema:name",
        "interstimulusInterval": "nsg:interstimulusInterval",
        "refreshRate": "nsg:refreshRate",
        "backgroundLuminance": "nsg:backgroundLuminance",
	    "hadProtocol":"prov:hadProtocol",
        "value": "schema:value",
    	"citation":"nsg:citation",
    	"code":"nsg:code",
    	"license":"nsg:license"
        }

    fields = (
        Field("name", basestring, "name", required=True),
        Field("stimulus", VisualStimulus, "used", required=True),
        Field("experiment", ("electrophysiology.ElectrodeArrayExperiment", "electrophysiology.EEGExperiment", "electrophysiology.ECoGExperiment", "electrophysiology.PatchClampExperiment", "electrophysiology.ExtracellularElectrodeExperiment", "optophysiology.TwoPhotonImaging", "electrophysiology.ElectrodeArrayExperiment"), "wasInformedBy"),
        Field("interstimulus_interval", QuantitativeValue, "interstimulusInterval"),
        Field("refresh_rate", QuantitativeValue, "refreshRate"),
        Field("background_luminance", QuantitativeValue, "backgroundLuminance"),
        Field("protocol", Protocol, "hadProtocol"),
    	Field("citation", basestring, "citation"),
    	Field("code", basestring, "code"),
    	Field("license", License, "license")
    )

    def __init__(self, name, stimulus, experiment=None, interstimulus_interval=None, refresh_rate=None, background_luminance=None, protocol=None, citation=None, code=None, license=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class ElectrophysiologicalStimulus(KGObject):
    """A generic electrophysiological stimulus."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/electrophysiologicalstimulus/v0.1.0"
    type = ["nsg:ElectrophysiologicalStimulus", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "minds": "https://schema.hbp.eu/",
        "name": "schema:name",
        "description": "schema:description",
        "distribution": {
            "@id": "schema:distribution",
            "@type": "@id"},
        "downloadURL": {
            "@id": "schema:downloadURL",
            "@type": "@id"},
        "mediaType": {
            "@id": "schema:mediaType"
        }
    }
    fields = (
        Field("name", basestring, "name", required=True),
        Field("description", basestring, "description", required=True),
        Field("distribution", Distribution, "distribution"),
        Field("stimulation", "experiment.ElectrophysiologicalStimulation", "^prov:used", reverse="stimulus")
    )

    def __init__(self, name, description, distribution=None, stimulation=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class ElectrophysiologicalStimulation(KGObject):
    """Use of an electrophysiological stimulus in the experiment."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/electrophysiologicalstimulation/v0.1.0"
    type = ["nsg:ElectrophysiologicalStimulation", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "used": "prov:used",
        "wasInformedBy": "nsg:wasInformedBy",
        "name": "schema:name",
	    "hadProtocol": "prov:hadProtocol",
        "value": "schema:value",
    	"citation": "nsg:citation",
    	"code": "nsg:code",
    	"stimulusType": "nsg:stimulusType",
    	"license": "nsg:license"
        }

    fields = (
        Field("name", basestring, "name", required=True),
        Field("electrophysiological_stimulus", ElectrophysiologicalStimulus, "used", required=True),
        Field("experiment", ("experiment.ElectrodeArrayExperiment", "electrophysiology.EEGExperiment", "electrophysiology.ECoGExperiment", "electrophysiology.PatchClampExperiment", "electrophysiology.ExtracellularElectrodeExperiment", "optophysiology.TwoPhotonImaging", "electrophysiology.ElectrodeArrayExperiment"), "wasInformedBy"),
        Field("stimulus_type", StimulusType, "stimulusType"),
        Field("protocol", Protocol, "hadProtocol"),
    	Field("citation", basestring, "citation"),
    	Field("code", basestring, "code"),
    	Field("license", License, "license")
    )

    def __init__(self, name, electrophysiological_stimulus, experiment=None, stimulus_type=None, protocol=None, citation=None, code=None, license=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class BehavioralStimulus(KGObject):
    """A generic behavioral stimulus."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/behavioralstimulus/v0.1.0"
    type = ["nsg:BehavioralStimulus", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "minds": "https://schema.hbp.eu/",
        "name": "schema:name",
        "description": "schema:description",
        "distribution": {
            "@id": "schema:distribution",
            "@type": "@id"},
        "downloadURL": {
            "@id": "schema:downloadURL",
            "@type": "@id"},
        "mediaType": {
            "@id": "schema:mediaType"
        }
    }
    fields = (
        Field("name", basestring, "name", required=True),
        Field("description", basestring, "description", required=True),
        Field("distribution", Distribution, "distribution"),
        Field("stimulation", "experiment.BehavioralStimulation", "^prov:used", reverse="stimulus")
    )

    def __init__(self, name, description, distribution=None, stimulation=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class BehavioralStimulation(KGObject):
    """Use of an behavioral stimulus in the experiment."""
    namespace = DEFAULT_NAMESPACE
    _path = "/electrophysiology/behavioralstimulation/v0.1.0"
    type = ["nsg:BehavioralStimulation", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "used": "prov:used",
        "name": "schema:name",
	    "hadProtocol": "prov:hadProtocol",
        "value": "schema:value",
    	"citation": "nsg:citation",
    	"code": "nsg:code",
    	"stimulusType": "nsg:stimulusType",
    	"license": "nsg:license",
        "wasInformedBy" : "nsg:wasInformedBy",
        "distribution": {
            "@id": "schema:distribution",
            "@type": "@id"},
        "downloadURL": {
            "@id": "schema:downloadURL",
            "@type": "@id"},
        "mediaType": {
            "@id": "schema:mediaType"
        }
        }

    fields = (
        Field("name", basestring, "name", required=True),
        Field("behavioral_stimulus", BehavioralStimulus, "used", required=True),
        Field("experiment", ("electrophysiology.ElectrodeArrayExperiment", "electrophysiology.EEGExperiment", "electrophysiology.ECoGExperiment", "electrophysiology.PatchClampExperiment", "electrophysiology.ExtracellularElectrodeExperiment", "optophysiology.TwoPhotonImaging", "electrophysiology.ElectrodeArrayExperiment"), "wasInformedBy"),
        Field("CogPOID", Distribution, "distribution"),
        Field("CogAtlasID", Distribution, "distribution"),
        Field("protocol", Protocol, "hadProtocol"),
    	Field("citation", basestring, "citation"),
    	Field("code", basestring, "code"),
    	Field("license", License, "license")
    )

    def __init__(self, name, behavioral_stimulus, experiment=None, cogpoid=None, cogatlasid=None, protocol=None, citation=None, code=None, license=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)