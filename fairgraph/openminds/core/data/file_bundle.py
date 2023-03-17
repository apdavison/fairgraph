"""
Structured information on a bundle of file instances.
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class FileBundle(KGObject):
    """
    Structured information on a bundle of file instances.
    """
    default_space = "files"
    type_ = ["https://openminds.ebrains.eu/core/FileBundle"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the file bundle."),
        Field("content_description", str, "vocab:contentDescription", multiple=False, required=False,
              doc="no description available"),
        Field("format", "openminds.core.ContentType", "vocab:format", multiple=False, required=False,
              doc="Method of digitally organizing and structuring data or information."),
        Field("grouped_by", ["openminds.computation.LocalFile", "openminds.controlledterms.AnalysisTechnique", "openminds.controlledterms.AuditoryStimulusType", "openminds.controlledterms.BiologicalOrder", "openminds.controlledterms.BiologicalSex", "openminds.controlledterms.BreedingType", "openminds.controlledterms.CellCultureType", "openminds.controlledterms.CellType", "openminds.controlledterms.Disease", "openminds.controlledterms.DiseaseModel", "openminds.controlledterms.ElectricalStimulusType", "openminds.controlledterms.GeneticStrainType", "openminds.controlledterms.GustatoryStimulusType", "openminds.controlledterms.Handedness", "openminds.controlledterms.MolecularEntity", "openminds.controlledterms.OlfactoryStimulusType", "openminds.controlledterms.OpticalStimulusType", "openminds.controlledterms.Organ", "openminds.controlledterms.OrganismSubstance", "openminds.controlledterms.OrganismSystem", "openminds.controlledterms.Species", "openminds.controlledterms.StimulationApproach", "openminds.controlledterms.StimulationTechnique", "openminds.controlledterms.SubcellularEntity", "openminds.controlledterms.TactileStimulusType", "openminds.controlledterms.Technique", "openminds.controlledterms.TermSuggestion", "openminds.controlledterms.UBERONParcellation", "openminds.controlledterms.VisualStimulusType", "openminds.core.BehavioralProtocol", "openminds.core.File", "openminds.core.FileBundle", "openminds.core.Subject", "openminds.core.SubjectGroup", "openminds.core.SubjectGroupState", "openminds.core.SubjectState", "openminds.core.TissueSample", "openminds.core.TissueSampleCollection", "openminds.core.TissueSampleCollectionState", "openminds.core.TissueSampleState", "openminds.sands.CommonCoordinateSpace", "openminds.sands.CommonCoordinateSpaceVersion", "openminds.sands.CustomAnatomicalEntity", "openminds.sands.CustomCoordinateSpace", "openminds.sands.ParcellationEntityVersion"], "vocab:groupedBy", multiple=True, required=False,
              doc="Reference to the aspect used to group something."),
        Field("grouping_types", "openminds.controlledterms.FileBundleGrouping", "vocab:groupingType", multiple=True, required=False,
              doc="no description available"),
        Field("hash", "openminds.core.Hash", "vocab:hash", multiple=False, required=False,
              doc="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value."),
        Field("is_part_of", ["openminds.core.FileBundle", "openminds.core.FileRepository"], "vocab:isPartOf", multiple=False, required=True,
              doc="Reference to the ensemble of multiple things or beings."),
        Field("storage_size", "openminds.core.QuantitativeValue", "vocab:storageSize", multiple=False, required=False,
              doc="Quantitative value defining how much disk space is used by an object on a computer system."),

    ]
    existence_query_fields = ('name', 'is_part_of')

    def __init__(self, name=None, content_description=None, format=None, grouped_by=None, grouping_types=None, hash=None, is_part_of=None, storage_size=None, id=None, data=None, space=None, scope=None):
        return super().__init__(id=id, data=data, space=space, scope=scope, name=name, content_description=content_description, format=format, grouped_by=grouped_by, grouping_types=grouping_types, hash=hash, is_part_of=is_part_of, storage_size=storage_size)