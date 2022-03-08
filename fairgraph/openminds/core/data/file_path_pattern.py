"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import EmbeddedMetadata, IRI
from fairgraph.fields import Field




class FilePathPattern(EmbeddedMetadata):
    """

    """
    type = ["https://openminds.ebrains.eu/core/FilePathPattern"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("grouping_type", "openminds.controlledterms.FileBundleGrouping", "vocab:groupingType", multiple=False, required=True,
              doc="no description available"),
        Field("regex", str, "vocab:regex", multiple=False, required=True,
              doc="no description available"),

    ]
