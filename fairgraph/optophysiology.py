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
from .commons import QuantitativeValue, BrainRegion, Origin, CellType, StimulusType, License, Shape
from .core import Subject, Person, Protocol
from .minds import Dataset
from .utility import compact_uri, standard_context, as_list
#from .electrophysiology import Trace

DEFAULT_NAMESPACE = "neuralactivity"

class RegionOfInterest(KGObject):
    """A region of interest within an image sequence."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/regionofinterest/v0.0.2"
    type = ["prov:Entity", "nsg:RegionOfInterest"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/pdrov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
	"origin": "nsg:origin",
        "x": "nsg:x",
        "y": "nsg:y",
        "shape": "nsg:shape",
	"description":"nsg:description",
	"classification":"nsg:classification"
    }
    fields = (
        Field("name", basestring, "name", required=True),
        Field("origin", Origin, "nsg:origin", required=True),
        Field("x", float, "x", required=True),
        Field("y", float, "y", required=True),
        Field("shape", Shape, "nsg:shape"),
        Field("size", basestring, "size"),
	Field("classification", basestring, "classification"),
	Field("description", basestring, "description")
    )

    def __init__(self, name, origin, x, y, shape=None, size=None, classification=None, description=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class FluorescenceTrace(KGObject):
    """A time series representing the ΔF/F signal within a region of interest"""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/fluorescencetrace/v0.3.0"
    type = ["prov:Entity", "nsg:FluorescenceTrace"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "timeStep": "nsg:timeStep",
        "value": "schema:value",
        "description": "schema:description",
        "wasGeneratedBy": "prov:wasGeneratedBy",
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
        Field("time_step", QuantitativeValue, "timeStep", required=True),
        Field("generated_by", "optophysiology.TimeSeriesExtraction", "wasGeneratedBy"),
        Field("description", basestring, "description"),
        Field("distribution", Distribution, "distribution")
    )

    def __init__(self, name, time_step, generated_by=None, description=None, distribution=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class TimeSeriesExtraction(KGObject):
    """Process of transforming the series of fluorescence responses within a Region of Interest into a ΔF/F signal"""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/timeseriesextraction/v0.1.0"
    type = ["prov:Activity", "nsg:TimeSeriesExtraction"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "timeStep": "nsg:timeStep",
        "value": "schema:value",
        "description": "schema:description",
        "wasGeneratedBy": "prov:wasGeneratedBy",
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
        Field("fluorescence_trace", FluorescenceTrace, "generated", required=True),
        Field("region_of_interest", RegionOfInterest, "used", required=True),
        Field("protocol", Protocol, "hadProtocol"),
        Field("people", Person, "wasAssociatedWith", multiple=True),
    	Field("citation", basestring, "citation"),
    	Field("code", basestring, "code"),
    	Field("license", License, "license")
        )

    def __init__(self, fluorescence_trace, region_of_interest, protocol=None, people=None, citation=None, code=None, license=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class ImageSequence(KGObject):
    """A sequence of images in the same imaging plane, produced by scanning optical microscopy."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/imagesequence/v0.4.0"
    type = ["prov:Entity", "nsg:ImageSequence"]
    context = {
            "schema": "http://schema.org/",
            "prov": "http://www.w3.org/ns/prov#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
            "name": "schema:name",
            "frameRate": "nsg:frameRate",
            "imageCount": "nsg:imageCount",
            "imageSize": "nsg:imageSize",
            "brainLocation": "nsg:brainLocation",
            "value": "schema:value",
            "description": "schema:description",
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
            "minds": "https://schema.hbp.eu/"
            }

    fields = (
        Field("name", basestring, "name", required=True),
        Field("frame_rate", QuantitativeValue, "FrameRate", required=True),
        Field("generated_by", "optophysiology.TwoPhotoImaging", "wasGeneratedBy"),
        Field("image_count", int, "ImageCount", required=False),
        Field("image_size", int, "ImageSize", required=False),
        Field("brain_location", BrainRegion, "brainRegion", required=False, multiple=True),
        Field("distribution", Distribution, "distribution", required=False),
        Field("description", basestring, "description", required=False)
    )

    def __init__(self, name, frame_rate, generated_by=None, image_count=None, image_size=None, brain_location=None, distribution=None, description=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class ROISelection(KGObject):
    """Process of selecting regions of interest, may be manual, semi-automated, or fully automated."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/roiselection/v0.1.0"
    type = ["prov:Activity", "nsg:ROISelection"]
    context = {
        "schema": "http://schema.org/",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "generated": "prov:generated",
        "used": "prov:used",
	"hadProtocol":"prov:hadProtocol",
        "wasAssociatedWith": "prov:wasAssociatedWith",
	"citation":"nsg:citation",
	"code":"nsg:code",
	"license":"nsg:license"
    }
    fields = (
        Field("image_sequence", ImageSequence, "used", required=True),
        Field("regions", RegionOfInterest, "generated", required=True),
        Field("protocol", Protocol, "hadProtocol"),
        Field("people", Person, "wasAssociatedWith", multiple=True),
	Field("citation", basestring, "citation"),
	Field("code", basestring, "code"),
	Field("license", License, "license")
    )

    def __init__(self, image_sequence, regions, protocol=None, people=None, citation=None, code=None, license=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class CranialWindow(KGObject):
    """A window (partially) through the skull."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/cranialwindow/v0.1.0"
    type = ["prov:Entity", "nsg:CranialWindow"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "value": "schema:value",
        "name": "schema:name",
        "brainLocation": "nsg:brainLocation",
	"windowType":"nsg:windowType",
	"diameter":"nsg:diameter",
	"fluorescenceLabeling":"nsg:fluorescenceLabeling",
        "description": "schema:description",
        "wasGeneratedBy": "prov:wasGeneratedBy",
        "minds": "https://schema.hbp.eu/"
    }
    fields = (
        Field("name", basestring, "name", required=True),
        Field("brain_location", BrainRegion, "brainRegion", multiple=True),
        Field("window_type", basestring, "windowType"),
        Field("diameter", QuantitativeValue, "diameter"),
        Field("fluorescence_labeling", basestring, "fluorescenceLabeling"),
        Field("description", basestring, "description"),
        Field("generated_by", "optophysiology.Craniotomy", "wasGeneratedBy")
    )

    def __init__(self, name, brain_location=None, window_type=None, diameter=None, fluorescence_labeling=None, description=None, generated_by=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class Craniotomy(KGObject):
    """Surgical procedure to give optical access through the skull to the brain (dura)."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/craniotomy/v0.1.0"
    type = ["prov:Activity", "nsg:Craniotomy"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "generated": "prov:generated",
        "used": "prov:used",
        "anesthesia": "nsg:anesthesia",
        "startedAtTime": "prov:startedAtTime",
        "endedAtTime": "prov:endedAtTime",
	"hadProtocol": "hadProtocol"
    }
    fields = (
        Field("subject", Subject, "used", required=True),
        Field("cranial_window", CranialWindow, "generated", required=True),
        Field("anesthesia", basestring, "anesthesia"),
	Field("protocol", Protocol, "hadProtocol"),
        Field("start_time", datetime, "startedAtTime"),
        Field("end_time", datetime, "endedAtTime"),
        Field("people", Person, "wasAssociatedWith", multiple=True)
    )

    def __init__(self, subject, cranial_window, anesthesia=None, protocol=None, start_time=None, end_time=None, people=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class TwoPhotonImaging(KGObject):
    """Two-photon-excited fluorescence laser-scanning microscopy."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/twophotonimaging/v0.2.0"
    type = ["prov:ExperimentalActivity", "nsg:TwoPhotonImaging"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "generated": "prov:generated",
        "used": "prov:used",
        "value": "schema:value",
        "microscope": "nsg:microscope",
        "brainState": "nsg:brainState",
        "anesthesia": "nsg:anesthesia",
        "laser": "nsg:laser",
        "excitationWavelength": "nsg:excitationWavelength",
        "laserPower": "nsg:laserPower",
        "collectionWavelength": "nsg:collectionWavelength",
        "imagingDepth": "nsg:imagingDepth",
        "startedAtTime": "prov:startedAtTime",
        "wasAssociatedWith": "prov:wasAssociatedWith",
        "endedAtTime": "prov:endedAtTime",
	"hadProtocol": "prov:hadProtocol"
    }
    fields = (
        Field("cranial_window", CranialWindow, "used", required=True),
        Field("image_sequence", ImageSequence, "generated", required=True),
        Field("microscope", basestring, "microscope"),
        Field("brain_state", basestring, "brainState"),
        Field("anesthesia", basestring, "anesthesia"),
        Field("laser", basestring, "laser"),
        Field("excitation_wavelength", QuantitativeValue, "excitationWavelength"),
        Field("power_at_objective", QuantitativeValue, "laserPower"),
        Field("collection_wavelength", QuantitativeValue, "collectionWavelength"),
        Field("imaging_depth", QuantitativeValue, "imagingDepth"),
        Field("start_time", datetime, "startedAtTime"),
        Field("end_time", datetime, "endedAtTime"),
	Field("protocol", Protocol, "hadProtocol"),
        Field("people", Person, "wasAssociatedWith", multiple=True)
    )

    def __init__(self, cranial_window, image_sequence, microscope=None, brain_state=None, anesthesia=None, laser=None, excitation_wavelength=None, power_at_objective=None, collection_wavelength=None, imaging_depth=None, start_time=None, end_time=None, protocol=None, people=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class MotionCorrection(KGObject):
    """Correction for x-y movement in image frames."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/motioncorrection/v0.1.0"
    type = ["nsg:MotionCorrection", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "generated": "prov:generated",
        "used": "prov:used",
	"hadProtocol":"prov:hadProtocol",
        "wasAssociatedWith": "prov:wasAssociatedWith",
	"citation":"nsg:citation",
	"code":"nsg:code",
	"license":"nsg:license"
    }
    fields = (
        Field("before", ImageSequence, "used", required=True),
        Field("after", ImageSequence, "generated", required=True),
        Field("protocol", Protocol, "hadprotocol"),
        Field("people", Person, "wasAssociatedWith", multiple=True),
	Field("citation", basestring, "citation"),
	Field("code", basestring, "code"),
	Field("license", License, "license")
    )

    def __init__(self, before, after, protocol=None, people=None, citation=None, code=None, license=None, id=None, instance=None):
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
                compacted_types = compact_uri(D["@type"], standard_context)
                if otype not in compacted_types:
                    print("Warning: type mismatch {} - {}".format(otype, compacted_types))
        args = {}
        for field in cls.fields:
            if field.intrinsic:
                data_item = D.get(field.path)
            else:
                data_item = D["@id"]
            args[field.name] = field.deserialize(data_item, client)
        obj = cls(id=D["@id"], instance=instance, **args)
        return obj

    def _build_data(self, client):
        """docstring"""
        data = super(MotionCorrection, self)._build_data(client)

    def resolve(self, client, api="query"):
        if hasattr(self.before, "resolve"):
            self.before = self.before.resolve(client, api=api)
        if hasattr(self.after, "resolve"):
            self.after = self.after.resolve(client, api=api)
        for i, person in enumerate(self.people):
            if hasattr(person, "resolve"):
                self.people[i] = person.resolve(client, api=api)


class VisualStimulus(KGObject):
    """A generic visual stimulus."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/visualstimulus/v0.1.0"
    type = ["prov:Entity", "nsg:VisualStimulus"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "value": "schema:value",
        "name": "schema:name",
        "description": "schema:description",
        "minds": "https://schema.hbp.eu/",
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
        Field("distribution", Distribution, "distribution")
    )

    def __init__(self, name, description=None, distribution=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class VisualStimulation(KGObject):
    """Presentation of a visual stimulus to the subject of the experiment."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/visualstimulation/v0.1.1"
    type = ["prov:Activity", "nsg:VisualStimulation"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "used": "prov:used",
	"protocol":"prov:hadProtocol",
        "value": "schema:value",
	"citation":"nsg:citation",
	"code":"nsg:code",
	"license":"nsg:license"
    }
    fields = (
        Field("visual_stimulus", VisualStimulus, "used", required=True),
        Field("interstimulus_interval", QuantitativeValue, "interstimulusInterval"),
        Field("refresh_rate", QuantitativeValue, "refreshRate"),
        Field("background_luminance", QuantitativeValue, "backgroundLuminance"),
        Field("protocol", Protocol, "hadProtocol"),
	Field("citation", basestring, "citation"),
	Field("code", basestring, "code"),
	Field("license", License, "license")
    )

    def __init__(self, visual_stimulus, interstimulus_interval=None, refresh_rate=None, background_luminance=None, citation=None, protocol=None, code=None, license=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)
