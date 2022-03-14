"""
Metadata for entities that are used in multiple experimental contexts (e.g. in both electrophysiology and optophysiology).

"""


# Copyright 2018-2020 CNRS

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime
from .base_v2 import KGObject, cache, Distribution
from .fields import Field
from .commons import QuantitativeValue, QuantitativeValueRange, BrainRegion, License, CultureType, StimulusType
from .core import Subject, Person, Protocol
from .utility import compact_uri, standard_context, as_list


DEFAULT_NAMESPACE = "neuralactivity"


class Device(KGObject):
    """Device used to collect recording in ElectrodeArrayExperiment"""
    namespace = DEFAULT_NAMESPACE
    _path = "/electrophysiology/device/v0.1.0"
    type = ["nsg:Device", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "manufacturer" : "nsg:manufacturer",
        "modelName" : "nsg:modelName",
        "softwareVersion" : "nsg:softwareVersion",
        "serialNumber" : "nsg:serialNumber",
        "distribution": {
            "@id": "schema:distribution",
            "@type": "@id"},
        "downloadURL": {
            "@id": "schema:downloadURL",
            "@type": "@id"},
        "mediaType": {
            "@id": "schema:mediaType",
        "description": "schema:description"
        }
    }
    fields = (
        Field("name", str, "name", required=True),
        Field("manufacturer", str, "manufacturer"),
        Field("model_name", str, "modelName"),
        Field("software_version", str, "softwareVersion"),
        Field("serial_number", str, "serialNumber"),
        Field("distribution", Distribution, "distribution"),
        Field("description", str, "description"),
        Field("placement_activity", ("electrophysiology.ElectrodePlacementActivity", "electrophysiology.ElectrodeImplantationActivity"), "^prov:generated", reverse="device"),
        Field("experiment", ("electrophysiology.ElectrodeArrayExperiment", "electrophysiology.EEGExperiment", "electrophysiology.ECoGExperiment"), "^prov:used", reverse="device")
    )

    def __init__(self, name, manufacturer=None, model_name=None, software_version=None, serial_number=None,
    distribution=None, description=None, placement_activity=None, experiment=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


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
        "minds": "https://schema.hbp.eu/",
        "value": "schema:value",
        "name": "schema:name",
        "brainLocation": "nsg:brainLocation",
        "brainRegion": "nsg:brainRegion",
        "windowType":"nsg:windowType",
        "diameter":"nsg:diameter",
        "fluorescenceLabeling":"nsg:fluorescenceLabeling",
        "description": "schema:description"
        }
    fields = (
        Field("name", str, "name", required=True),
        Field("brain_location", BrainRegion, "brainRegion", multiple=True),
        Field("window_type", str, "windowType"),
        Field("diameter", QuantitativeValue, "diameter"),
        Field("fluorescence_labeling", str, "fluorescenceLabeling"),
        Field("description", str, "description"),
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
        "used": "prov:used",
        "generated": "prov:generated",
        "anesthesia": "nsg:anesthesia",
        "hadProtocol": "prov:hadProtocol",
        "startedAtTime": "prov:startedAtTime",
        "endedAtTime": "prov:endedAtTime",
        "wasAssociatedWith": "prov:wasAssociatedWith"
    }
    fields = (
        Field("name", str, "name", required=True),
        Field("subject", Subject, "used", required=True),
        Field("cranial_window", CranialWindow, "generated", required=True),
        Field("anesthesia", str, "anesthesia"),
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
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "providerId": "nsg:providerId",
        "wasDerivedFrom": "prov:wasDerivedFrom"
    }
    fields = (
        Field("name", str, "name", required=True),
        Field("subject", Subject, "wasDerivedFrom", required=True),
        Field("provider_id", str, "providerId"),
        Field("brain_slicing_activity", "experiment.BrainSlicingActivity", "^prov:generated", reverse="slices"),
        #Field("activity", ("electrophysiology.PatchClampActivity", "optophysiology.TwoPhotonImaging"), "^prov:used", reverse=["recorded_tissue","target"])
        #  support for multiple reverses not implemented
        Field("activity", ("electrophysiology.PatchClampActivity", "optophysiology.TwoPhotonImaging"), "^prov:used", reverse="recorded_tissue")
    )


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
        "label": "rdfs:label",
        "value": "schema:value",
        "unitCode": "schema:unitCode",
        "brainLocation": "nsg:brainLocation",
        "brainRegion": "nsg:brainRegion",
        "hemisphere": "nsg:hemisphere",
        "slicingPlane": "nsg:slicingPlane",
        "slicingAngle": "nsg:slicingAngle",
        "solution": "nsg:solution",
        "cuttingThickness": "nsg:cuttingThickness",
        "startedAtTime": "prov:startedAtTime",
        "endedAtTime": "prov:endedAtTime",
        "wasAssociatedWith": "prov:wasAssociatedWith"
    }
    fields = (
        Field("subject", Subject, "used", required=True),
        Field("slices", Slice, "generated", multiple=True, required=True),
        Field("brain_location", BrainRegion, "brainRegion", multiple=True),
        Field("hemisphere", str, "hemisphere"), # choice of Left, Right
        Field("slicing_plane", str, "slicingPlane"), # Sagittal, Para-sagittal, Coronal, Horizontal
        Field("slicing_angle", float, "slicingAngle"),
        Field("cutting_solution", str, "solution"),
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
                    print(f"Warning: type mismatch {otype} - {compacted_types}")
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
        Field("name", str, "name", required=True),
        Field("description", str, "description"),
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
        "name": "schema:name",
        "interstimulusInterval": "nsg:interstimulusInterval",
        "refreshRate": "nsg:refreshRate",
        "backgroundLuminance": "nsg:backgroundLuminance",
        "hadProtocol":"prov:hadProtocol",
        "citation":"nsg:citation",
        "code":"nsg:code",
        "license":"nsg:license"
        }

    fields = (
        Field("name", str, "name", required=True),
        Field("stimulus", VisualStimulus, "used", required=True),
        Field("experiment", ("electrophysiology.ElectrodeArrayExperiment", "electrophysiology.EEGExperiment", "electrophysiology.ECoGExperiment", "electrophysiology.PatchClampExperiment", "electrophysiology.ExtracellularElectrodeExperiment", "optophysiology.TwoPhotonImaging", "electrophysiology.ElectrodeArrayExperiment"), "^nsg: wasInformedBy", reverse="stimulation"),
        Field("interstimulus_interval", QuantitativeValue, "interstimulusInterval"),
        Field("refresh_rate", QuantitativeValue, "refreshRate"),
        Field("background_luminance", QuantitativeValue, "backgroundLuminance"),
        Field("protocol", Protocol, "hadProtocol"),
        Field("citation", str, "citation"),
        Field("code", str, "code"),
        Field("license", License, "license")
    )

    def __init__(self, name, stimulus, experiment=None, interstimulus_interval=None, refresh_rate=None,
    background_luminance=None, protocol=None, citation=None, code=None, license=None, id=None, instance=None):
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
        Field("name", str, "name", required=True),
        Field("description", str, "description", required=True),
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
        "name": "schema:name",
        "used": "prov:used",
        "hadProtocol": "prov:hadProtocol",
        "value": "schema:value",
        "citation": "nsg:citation",
        "code": "nsg:code",
        "license": "nsg:license"
        }

    fields = (
        Field("name", str, "name", required=True),
        Field("stimulus", ElectrophysiologicalStimulus, "used", required=True),
        Field("experiment", ("electrophysiology.ElectrodeArrayExperiment", "electrophysiology.EEGExperiment",
                             "electrophysiology.ECoGExperiment", "electrophysiology.PatchClampExperiment",
                             "electrophysiology.ExtracellularElectrodeExperiment", "optophysiology.TwoPhotonImaging",
                             "electrophysiology.ElectrodeArrayExperiment"), "^nsg: wasInformedBy", reverse="stimulation"),
        Field("protocol", Protocol, "hadProtocol"),
        Field("citation", str, "citation"),
        Field("code", str, "code"),
        Field("license", License, "license")
    )

    def __init__(self, name, stimulus, experiment=None, protocol=None, citation=None,
    code=None, license=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class BehavioralStimulus(KGObject):
    """A generic behavioral stimulus."""
    namespace = DEFAULT_NAMESPACE
    _path = "/experiment/behavioralstimulus/v0.1.0"
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
        Field("name", str, "name", required=True),
        Field("description", str, "description", required=True),
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
    _path = "/experiment/behavioralstimulation/v0.1.1"
    type = ["nsg:BehavioralStimulation", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "name": "schema:name",
        "used": "prov:used",
        "hadProtocol": "prov:hadProtocol",
        "citation": "nsg:citation",
        "code": "nsg:code",
        "license": "nsg:license"
        }

    fields = (
        Field("name", str, "name", required=True),
        Field("stimulus", BehavioralStimulus, "used", required=True),
        Field("experiment", ("electrophysiology.ElectrodeArrayExperiment", "electrophysiology.EEGExperiment", "electrophysiology.ECoGExperiment", "electrophysiology.PatchClampExperiment", "electrophysiology.ExtracellularElectrodeExperiment", "optophysiology.TwoPhotonImaging", "electrophysiology.ElectrodeArrayExperiment"), "^nsg: wasInformedBy", reverse="stimulation"),
        Field("protocol", Protocol, "hadProtocol"),
        Field("citation", str, "citation"),
        Field("code", str, "code"),
        Field("license", License, "license")
    )

    def __init__(self, name, stimulus, experiment=None, protocol=None, citation=None, code=None, license=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)
