"""
Structured information on a software tool (concept level).
"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Software(KGObject):
    """
    Structured information on a software tool (concept level).
    """
    default_space = "software"
    type = ["https://openminds.ebrains.eu/core/Software"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the software."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the software."),
        Field("custodians", ["openminds.core.Organization", "openminds.core.Person"], "vocab:custodian", multiple=True, required=False,
              doc="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product."),
        Field("description", str, "vocab:description", multiple=False, required=True,
              doc="Longer statement or account giving the characteristics of the software."),
        Field("developers", ["openminds.core.Organization", "openminds.core.Person"], "vocab:developer", multiple=True, required=True,
              doc="Legal person that creates or improves products or services (e.g., software, applications, etc.)."),
        Field("digital_identifier", ["openminds.core.DOI", "openminds.core.SWHID"], "vocab:digitalIdentifier", multiple=False, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("versions", "openminds.core.SoftwareVersion", "vocab:hasVersion", multiple=True, required=True,
              doc="Reference to variants of an original."),
        Field("homepage", "openminds.core.URL", "vocab:homepage", multiple=False, required=False,
              doc="Main website of the software."),
        Field("how_to_cite", str, "vocab:howToCite", multiple=False, required=False,
              doc="Preferred format for citing a particular object or legal person."),

    ]
    existence_query_fields = ('alias',)
