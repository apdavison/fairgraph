"""
Metadata for morphology experiments.
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
from .base_v2 import KGObject, KGQuery, cache, Distribution
from .fields import Field
from .commons import QuantitativeValue, MorphologyType, BrainRegion, SomaType, ObjectiveType
from .core import Subject, Person, Protocol
from .minds import Dataset
from .utility import compact_uri, standard_context, as_list
from .experiment import Slice
from .electrophysiology import PatchedCell,  PatchedSlice
from .optophysiology import Position


DEFAULT_NAMESPACE = "neuralactivity"

class LabeledCell(KGObject):
    """A labeled cell used in a morphology study."""
    namespace = DEFAULT_NAMESPACE
    _path = "/morphology/labeledcell/v0.1.1"
    type = ["nsg:LabeledCell", "prov:Entity"]
    query_id = "fgModified"
    query_id_resolved = "fgResolvedModified"
    collection_class = "LabeledCellCollection"
    experiment_class = "PatchClampExperiment"
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "brainRegion": "nsg:brainRegion",
        "mType": "nsg:mType",
        "position": "nsg:position",
        "spatialCellName": "nsg:spatialCellName",
        "reconstructionRequested": "nsg:reconstructionRequested",
        "reconstructable": "nsg:reconstructable"
    }
    fields = (
        Field("name", str, "name", required=True),
        Field("project_name", str, "projectName"),
        Field("brain_location", BrainRegion, "brainRegion", multiple=True),
        Field("morphology_type", MorphologyType, "mType"), # specifies the coordinates of the location of the cell in the slice
        Field("location_in_slice", Position, "position"), #change to 3Dvector
        Field("spatial_cell_name", str, "spatialCellName"), # spatial cell name given during the annotation process
        Field("reconstruction_requested", bool, "reconstructionRequested"), # indicates if reconstruction the cell has been requested or not
        Field("reconstructable", bool, "reconstructable"), #indicates if the cell can be reconstructed or not
        Field("patched_cell", PatchedCell, "wasRevisionOf"),
        Field("collection", "morphology.LabeledCellCollection", "^prov:hadMember",
              reverse="labeled_cell") #chance reverse when labeledcellcollationmade
        )

    def __init__(self, name, project_name, brain_location, morphology_type=None,
    location_in_slice=None, spatial_cell_name=None, reconstruction_requested=None,
    reconstructable=None, patched_cell=None, collection=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class LabeledCellCollection(KGObject):
    """A collection of labeled cells."""
    namespace = DEFAULT_NAMESPACE
    _path = "/morphology/labeledcellcollection/v0.1.1"
    type = ["nsg:Collection"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "size": "schema:size",
        "hadMember": "prov:hadMember"
    }

    fields = (
        Field("name", str, "name", required=True),
        Field("cells", LabeledCell, "hadMember", required=True, multiple=True),
        Field("slice", "morphology.AnnotatedSlice", "^nsg:hasPart", reverse="recorded_cells") # chcek reverse
    )

    def __init__(self, name,cells, slice=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)

    @property
    def size(self):
        return len(self.cells)


class FixedStainedSlice(KGObject):
    """An fixed, stained slice from a morphology experiment."""
    namespace = DEFAULT_NAMESPACE
    _path = "/morphology/fixedstainedslice/v0.1.1/"
    type = ["nsg:FixedStainedSlice", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "dcterms": "http://purl.org/dc/terms/",
        "name": "schema:name",
        "wasRevisionOf": "prov:wasRevisionOf"
    }
    fields = (
        Field("name", str, "name", required=True),
        Field("patched_slice", PatchedSlice, "wasRevisionOf")
    )

    def __init__(self, name, patched_slice=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class AnnotatedSlice(KGObject):
    """An annotated slice from a morphology experiment."""
    namespace = DEFAULT_NAMESPACE
    _path = "/morphology/annotatedslice/v0.1.1/"
    type = ["nsg:AnnotatedSlice", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "dcterms": "http://purl.org/dc/terms/",
        "name": "schema:name",
        "annotationAngle": "nsg:annotationAngle",
        "annotatorComment": "nsg:annotatorComment",
        "hasPart": "schema:hasPart",
        "wasRevisionOf": "prov:wasRevisionOf"
    }
    fields = (
        Field("name", str, "name", required=True),
        Field("annotation_angle", QuantitativeValue, "annotationAngle"),
        Field("annotator_comment", str, "annotatorComment"),
        Field("cell_collection", LabeledCellCollection, "hasPart"),
        Field("fixed_stained_slice", FixedStainedSlice, "wasRevisionOf")
    )

    def __init__(self, name, annotation_angle=None, annotator_comment=None,
        cell_collection=None, fixed_stained_slice=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class ReconstructedCell(KGObject):
    """A reconstructed cell."""
    namespace = DEFAULT_NAMESPACE
    _path = "/morphology/reconstructedcell/v0.1.4"
    type = ["nsg:ReconstructedCell", "prov:Entity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "brainLocation": "nsg:brainLocation",
        "mType": "nsg:mType",
        "somaType": "nsg:somaType"
    }
    fields = (
        Field("name", str, "name", required=True),
        Field("soma_brain_location", BrainRegion, "brainLocation", multiple=True),
        Field("axon_projection", BrainRegion, "brainRegion", multiple=True),
        Field("morphology_type", MorphologyType, "mType"),
        Field("soma_type", SomaType, "somaType")
        )

    def __init__(self, name, soma_brain_location=None, axon_projection=None, morphology_type=None,
    soma_type=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class FixationStainingMounting(KGObject):
    """Fixing, Staining and Mounting activities description"""
    namespace = DEFAULT_NAMESPACE
    _path = "/morphology/fixationstainingmounting/v0.1.1"
    type = ["nsg:FixationStainingMounting", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "fixationMethod": "nsg:fixationMethod",
        "stain": "nsg:stain",
        "mountingMedia": "nsg:mountingMedia",
        "used": "prov:used",
        "generated": "prov:generated"
        }
    fields = (
        Field("name", str, "name", required=True),
        Field("fixation_method", str, "fixationMethod"),
        Field("stain", str, "stain"),
        Field("mounting_media", str, "mountingMedia"),
        Field("slice_used", Slice, "used"),
        Field("slice_generated", FixedStainedSlice, "generated")
    )

    def __init__(self, name, fixation_method=None, stain=None, mounting_media=None,
    slice_used=None, slice_generated=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class AcquisitionAnnotation(KGObject):
    """Acquisition and annotation activity"""
    namespace = DEFAULT_NAMESPACE
    _path = "/morphology/acquisitionannotation/v0.1.1"
    type = ["nsg:AcquisitionAnnotation", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "objectiveMagnification": "nsg:objectiveMagnification",
        "used": "prov:used",
        "generated": "prov:generated",
        }
    fields = (
        Field("name", str, "name", required=True),
        Field("objective_magnification", str, "objectiveMagnification"),
        Field("fixed_stained_slice", FixedStainedSlice, "used"),
        Field("annotated_slice", AnnotatedSlice, "generated")
    )

    def __init__(self, name, objective_magnification=None, fixed_stained_slice=None,
    annotated_slice=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)


class Reconstruction(KGObject):
    """Reconstruction activity"""
    namespace = DEFAULT_NAMESPACE
    _path = "/morphology/reconstruction/v0.1.2"
    type = ["nsg:Reconstruction", "prov:Activity"]
    context = {
        "schema": "http://schema.org/",
        "prov": "http://www.w3.org/ns/prov#",
        "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "name": "schema:name",
        "objectiveType": "nsg:objectiveType",
        "objectiveMagnification": "nsg:objectiveMagnification",
        "compressionCorrection": "nsg:compressionCorrection",
        "used": "prov:used",
        "generated": "prov:generated",
        }
    fields = (
        Field("name", str, "name", required=True),
        Field("objective_type", ObjectiveType, "objectiveType"),
        Field("objective_magnification", str, "objectiveMagnification"),
        Field("compression_correction", str, "compressionCorrection"),
        Field("labeled_cell", LabeledCell, "used"),
        Field("reconstructed_cell", ReconstructedCell, "generated")
        )

    def __init__(self, name, objective_type=None, compression_correction=None, labeled_cell=None,
    reconstructed_cell=None, id=None, instance=None):
        args = locals()
        args.pop("self")
        KGObject.__init__(self, **args)
