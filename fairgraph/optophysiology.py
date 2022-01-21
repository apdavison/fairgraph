"""
Metadata for electrophysiology experiments.

The following methods are currently supported:
    - patch clamp recording in brain slices
    - sharp electrode intracellular recording in brain slices

Coming soon:
    - patch clamp recordings in cultured neurons
    - extracellular electrode recording, including tetrodes and multi-electrode arrays

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


import sys
import inspect
from datetime import datetime
from .base_v2 import KGObject, Distribution
from .fields import Field
from .commons import QuantitativeValue, BrainRegion, License
from .core import Person, Protocol
from .experiment import CranialWindow, Slice, VisualStimulation, ElectrophysiologicalStimulation, BehavioralStimulation, Device


DEFAULT_NAMESPACE = "neuralactivity"


class Position(KGObject):
    """Location within a coordinate system."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/position/v0.1.0"
    type = ["nsg:Position", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "origin": "nsg:origin",
        "x": "nsg:x",
        "ycoordinate": "nsg:y"
        }
    fields = (
        Field("name", str, "name", required=True),
        Field("origin", str, "origin", required=True),
        Field("xcoordinate", float, "x"),
        Field("ycoordinate", float, "y")
        )

    def __init__(self, name, origin, xcoordinate=None, ycoordinate=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class FluorescenceTrace(KGObject):
    """A time series representing the ΔF/F signal within a region of interest"""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/fluorescencetrace/v0.1.0"
    type = ["nsg:FluorescenceTrace", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "timeStep": "nsg:timeStep",
        "value": "schema:value",
        "description": "schema:description",
        "fluorescenceLabeling": "nsg: fluorescenceLabeling",
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
        Field("time_step", QuantitativeValue, "timeStep", required=True),
        Field("fluorescence_labeling", str, "fluorescenceLabeling"),
        Field("time_series", "TimeSeriesExtraction", "^prov:generated", reverse="fluorescence_trace"),
        Field("description", str, "description"),
        Field("distribution", Distribution, "distribution")
    )

    def __init__(self, name, time_step, fluorescence_labeling, time_series=None, description=None, distribution=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class TimeSeriesExtraction(KGObject):
    """Process of transforming the series of fluorescence responses within a Region of Interest into a ΔF/F signal"""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/timeseriesextraction/v0.1.0"
    type = ["nsg:TimeSeriesExtraction", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "value": "schema:value",
        "used": "prov:used",
        "generated": "prov:generated",
        "hadProtocol":"p  rov:hadProtocol",
        "wasAssociatedWith": "prov:wasAssociatedWith",
        "citation":"nsg:citation",
        "code":"nsg:code",
        "license":"nsg:license"
        }
    fields = (
        Field("name", str, "name", required=True),
        Field("fluorescence_trace", FluorescenceTrace, "generated", required=True),
        Field("region_of_interest", "optophysiology.RegionOfInterest", "used"),
        Field("protocol", Protocol, "hadProtocol"),
        Field("people", Person, "wasAssociatedWith", multiple=True),
        Field("citation", str, "citation"),
        Field("code", str, "code"),
        Field("license", License, "license")
    )

    def __init__(self, name, fluorescence_trace, region_of_interest=None, protocol=None, people=None, citation=None, code=None, license=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class ImageSequence(KGObject):
    """A sequence of images in the same imaging plane, produced by scanning optical microscopy."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/imagesequence/v0.1.0"
    type = ["nsg:ImageSequence", "prov:Entity"]
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
        "extent": "nsg:extent",
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
        Field("name", str, "name", required=True),
        Field("frame_rate", QuantitativeValue, "FrameRate", required=True),
        Field("generated_by", "TwoPhotonImaging", "^prov:generated", reverse="image_sequence"),
        Field("image_count", int, "imageCount", required=False),
        Field("image_size", int, "imageSize", required=False), # assumed square
        Field("extent", QuantitativeValue, "extent"),
        Field("brain_location", BrainRegion, "brainRegion", required=False, multiple=True),
        Field("correction_activity", "optophysiology.MotionCorrection", "^prov:used", reverse=["before", "after"]),
        Field("distribution", Distribution, "distribution", required=False),
        Field("description", str, "description", required=False)
    )

    def __init__(self, name, frame_rate, generated_by=None, image_count=None, image_size=None,
    extent=None, brain_location=None, correction_activity=None, distribution=None, description=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class RegionOfInterest(KGObject):
    """A region of interest within an image sequence."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/regionofinterest/v0.9.0"
    type = ["nsg:RegionOfInterest", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "position": "nsg:position",
        "shape": "nsg:geometry",
        "description": "nsg:description",
        "classification": "nsg:classification"
        }

    fields = (
        Field("name", str, "name", required=True),
        Field("position", Position, "position"),
        Field("shape", str, "shape"),
        Field("classification", str, "classification"),
        Field("description", str, "description"),
        Field("selection", "optophysiology.ROISelection","^prov:generated", reverse="regions"),
        Field("time_series", TimeSeriesExtraction,"^prov:used", reverse="region_of_interest"),
    )

    def __init__(self, name, position=None, shape=None, classification=None,
    description=None, selection=None, time_series=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class ROISelection(KGObject):
    """Process of selecting regions of interest, may be manual, semi-automated, or fully automated."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/roiselection/v0.2.0"
    type = ["nsg:ROISelection", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "used": "prov:used",
        "generated": "prov:generated",
        "hadProtocol": "prov:hadProtocol",
        "wasAssociatedWith": "prov:wasAssociatedWith",
        "citation": "nsg:citation",
        "code": "nsg:code",
        "license": "nsg:license"
        }
    fields = (
        Field("name", str, "name", required=True),
        Field("image_sequence", ImageSequence, "used", required=True),
        Field("regions", RegionOfInterest, "generated", required=True),
        Field("protocol", Protocol, "hadProtocol"),
        Field("people", Person, "wasAssociatedWith", multiple=True),
        Field("citation", str, "citation"),
        Field("code", str, "code"),
        Field("license", License, "license")
    )

    def __init__(self, name, image_sequence, regions, protocol=None, people=None, citation=None, code=None, license=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class TwoPhotonImaging(KGObject):
    """Two-photon-excited fluorescence laser-scanning microscopy."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/twophotonimaging/v0.1.1"
    #type = ["prov:ExperimentalActivity", "nsg:TwoPhotonImaging"]
    type = ["nsg:TwoPhotonImaging", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "name": "schema:name",
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
        "minds": "https://schema.hbp.eu/",
        "generated": "prov:generated",
        "wasInformedBy": "nsg:wasInformedBy",
        "used": "prov:used",
        "startedAtTime": "prov:startedAtTime",
        "endedAtTime": "prov:endedAtTime",
        "hadProtocol": "prov:hadProtocol",
        "wasAssociatedWith": "prov:wasAssociatedWith",
        "device": "nsg:device",
        "brainState": "nsg:brainState",
        "anesthesia": "nsg:anesthesia",
        "imagingDepth": "nsg:imagingDepth",
        "laser": "nsg:laser",
        "laserPower": "nsg:laserPower",
        "excitationWavelength": "nsg:excitationWavelength",
        "collectionWavelength": "nsg:collectionWavelength"
            }

    fields = (
        Field("name", str, "name", required=True),
        Field("image_sequence", ImageSequence, "generated", required=True),
        Field("stimulation", (VisualStimulation, BehavioralStimulation, ElectrophysiologicalStimulation), "wasInformedBy"),
        Field("target", (Slice, CranialWindow), "used"),
        Field("microscope", Device, "device"),
        Field("brain_state", str, "brainState"),
        Field("anesthesia", str, "anesthesia"),
        Field("laser", str, "laser"),
        Field("excitation_wavelength", QuantitativeValue, "excitationWavelength"),
        Field("power_at_objective", QuantitativeValue, "laserPower"),
        Field("collection_wavelength", QuantitativeValue, "collectionWavelength"),
        Field("imaging_depth", QuantitativeValue, "imagingDepth"),
        Field("distribution", Distribution, "distribution"),
        Field("start_time", datetime, "startedAtTime"),
        Field("end_time", datetime, "endedAtTime"),
        Field("protocol", Protocol, "hadProtocol"),
        Field("people", Person, "wasAssociatedWith", multiple=True)
    )

    def __init__(self, name, image_sequence=None, stimulation=None, target=None, microscope=None, brain_state=None, anesthesia=None, laser=None, excitation_wavelength=None, power_at_objective=None, collection_wavelength=None, imaging_depth=None, distribution=None, start_time=None, end_time=None, protocol=None, people=None, citation=None, code=None, license=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class MotionCorrection(KGObject):
    """Correction for x-y movement in image frames."""
    namespace = DEFAULT_NAMESPACE
    _path = "/optophysiology/motioncorrection/v0.2.0"
    type = ["nsg:MotionCorrection", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "xsd": "http://www.w3.org/2001/XMLSchema#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "name": "schema:name",
        "generated": "prov:generated",
        "used": "prov:used",
        "hadProtocol": "prov:hadProtocol",
        "wasAssociatedWith": "prov:wasAssociatedWith",
        "citation":"nsg:citation",
        "code":"nsg:code",
        "license":"nsg:license"
        }
    fields = (
        Field("name", str, "name", required=True),
        Field("before", ImageSequence, "used", required=True),
        Field("after", ImageSequence, "generated", required=True),
        Field("protocol", Protocol, "hadprotocol"),
        Field("people", Person, "wasAssociatedWith", multiple=True),
        Field("citation", str, "citation"),
        Field("code", str, "code"),
        Field("license", License, "license")
    )

    def __init__(self, name, before, after, protocol=None, people=None, citation=None, code=None, license=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)
