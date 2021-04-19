"""
Structured information on the contribution made to a research product.
"""

# this file was auto-generated


from fairgraph.base import KGObject
from fairgraph.fields import Field


class Contribution(KGObject):
    """
    Structured information on the contribution made to a research product.
    """
    space = "model"
    type = ["https://openminds.ebrains.eu/core/Contribution"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("contribution_types", "openminds.controlledTerms.ContributionType", "vocab:contributionType", multiple=True, required=True,
              doc="Distinct class of what was given or supplied as a part or share."),
        Field("contributor", ["openminds.core.Organization", "openminds.core.Person"], "vocab:contributor", multiple=False, required=True,
              doc="Legal person that gave or supplied something as a part or share."),
        
    ]
    existence_query_fields = ('name',)