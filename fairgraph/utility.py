"""


"""

try:
    from urllib.parse import urlparse, quote_plus
except ImportError:  # Python 2
    from urlparse import urlparse
    from urllib import quote_plus
from pyld import jsonld


standard_context = {
    "dcterms": "http://purl.org/dc/terms/",
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/"
}


def expand_uri(uri_list, context):
    return tuple(jsonld.expand({
        "@type": uri_list,
        "@context": context
    })[0]["@type"])


def compact_uri(uri_list, context):
    return tuple(jsonld.compact({"@type": uri_list}, context)["@type"])


def namespace_from_id(id):
    parts = urlparse(id)
    path_parts = parts.path.split("/")
    assert path_parts[2] == "data"
    return path_parts[3]
