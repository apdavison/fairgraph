"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class LivePaper(KGObject):
    """

    """
    default_space = "livepapers"
    type = ["https://openminds.ebrains.eu/publications/LivePaper"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the live paper."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the live paper."),
        Field("authors", ["openminds.core.Organization", "openminds.core.Person"], "vocab:author", multiple=True, required=True,
              doc="Creator of a literary or creative work, as well as a dataset publication."),
        Field("custodians", ["openminds.core.Organization", "openminds.core.Person"], "vocab:custodian", multiple=True, required=False,
              doc="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product."),
        Field("description", str, "vocab:description", multiple=False, required=True,
              doc="Longer statement or account giving the characteristics of the live paper."),
        Field("digital_identifier", "openminds.core.DOI", "vocab:digitalIdentifier", multiple=False, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("versions", "openminds.publications.LivePaperVersion", "vocab:hasVersion", multiple=True, required=True,
              doc="Reference to variants of an original."),
        Field("homepage", "openminds.core.URL", "vocab:homepage", multiple=False, required=False,
              doc="Main website of the live paper."),
        Field("how_to_cite", str, "vocab:howToCite", multiple=False, required=False,
              doc="Preferred format for citing a particular object or legal person."),

    ]
    existence_query_fields = ('name', 'alias')
