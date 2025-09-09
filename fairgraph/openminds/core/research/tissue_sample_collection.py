"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import TissueSampleCollection as OMTissueSampleCollection
from fairgraph import KGObject


class TissueSampleCollection(KGObject, OMTissueSampleCollection):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/TissueSampleCollection"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "has_parts",
            "openminds.latest.core.TissueSample",
            "isPartOf",
            reverse="is_part_of",
            multiple=True,
            description="reverse of 'is_part_of'",
        ),
        Property(
            "has_study_results_in",
            "openminds.latest.core.DatasetVersion",
            "studiedSpecimen",
            reverse="studied_specimens",
            multiple=True,
            description="reverse of 'studied_specimens'",
        ),
        Property(
            "is_used_to_group",
            "openminds.latest.core.FileBundle",
            "groupedBy",
            reverse="grouped_by",
            multiple=True,
            description="reverse of 'grouped_by'",
        ),
        Property(
            "used_in",
            ["openminds.latest.sands.BrainAtlasVersion", "openminds.latest.sands.CommonCoordinateSpaceVersion"],
            "usedSpecimen",
            reverse="used_specimens",
            multiple=True,
            description="reverse of 'used_specimens'",
        ),
    ]
    existence_query_properties = ("lookup_label",)

    def __init__(
        self,
        lookup_label=None,
        additional_remarks=None,
        anatomical_locations=None,
        biological_sexes=None,
        has_parts=None,
        has_study_results_in=None,
        internal_identifier=None,
        is_used_to_group=None,
        lateralities=None,
        number_of_tissue_samples=None,
        origins=None,
        species=None,
        studied_states=None,
        types=None,
        used_in=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            lookup_label=lookup_label,
            additional_remarks=additional_remarks,
            anatomical_locations=anatomical_locations,
            biological_sexes=biological_sexes,
            has_parts=has_parts,
            has_study_results_in=has_study_results_in,
            internal_identifier=internal_identifier,
            is_used_to_group=is_used_to_group,
            lateralities=lateralities,
            number_of_tissue_samples=number_of_tissue_samples,
            origins=origins,
            species=species,
            studied_states=studied_states,
            types=types,
            used_in=used_in,
        )


# cast openMINDS instances to their fairgraph subclass
TissueSampleCollection.set_error_handling(None)
for key, value in OMTissueSampleCollection.__dict__.items():
    if isinstance(value, OMTissueSampleCollection):
        fg_instance = TissueSampleCollection.from_jsonld(value.to_jsonld())
        fg_instance._space = TissueSampleCollection.default_space
        setattr(TissueSampleCollection, key, fg_instance)
TissueSampleCollection.set_error_handling("log")
