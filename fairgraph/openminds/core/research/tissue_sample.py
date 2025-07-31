"""
Structured information on a tissue sample.
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.core import TissueSample
from fairgraph import KGObject


class TissueSample(KGObject, TissueSample):
    """
    Structured information on a tissue sample.
    """

    type_ = "https://openminds.om-i.org/types/TissueSample"
    default_space = "dataset"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
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
        anatomical_locations=None,
        biological_sex=None,
        has_study_results_in=None,
        internal_identifier=None,
        is_part_of=None,
        is_used_to_group=None,
        lateralities=None,
        origin=None,
        species=None,
        studied_states=None,
        type=None,
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
            anatomical_locations=anatomical_locations,
            biological_sex=biological_sex,
            has_study_results_in=has_study_results_in,
            internal_identifier=internal_identifier,
            is_part_of=is_part_of,
            is_used_to_group=is_used_to_group,
            lateralities=lateralities,
            origin=origin,
            species=species,
            studied_states=studied_states,
            type=type,
            used_in=used_in,
        )
