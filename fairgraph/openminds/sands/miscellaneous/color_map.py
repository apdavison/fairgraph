"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class ColorMap(KGObject):
    """

    """
    default_space = "atlas"
    type_ = ["https://openminds.ebrains.eu/sands/ColorMap"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the color map."),
        Field("code_source", str, "vocab:codeSource", multiple=False, required=True,
              doc="no description available"),
        Field("programming_language", "openminds.controlledterms.ProgrammingLanguage", "vocab:programmingLanguage", multiple=False, required=True,
              doc="Distinct set of instructions for computer programs in order to produce various kinds of output."),

    ]
    existence_query_fields = ('name', 'code_source', 'programming_language')
