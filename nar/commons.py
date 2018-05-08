# encoding: utf-8
"""

"""

import collections
#from typing import NamedTuple
from .base import KGObject, KGProxy


#class Address(NamedTuple):
#    locality: str
#    country: str

Address = collections.namedtuple('Address', ['locality', 'country'])


class OntologyTerm(object):
    """docstring"""

    def __init__(self, label, iri=None):
        self.label = label
        self.iri = iri or self.iri_map[label]

    def __repr__(self):
        #return (f'{self.__class__.__name__}('
        #        f'{self.label!r}, {self.iri!r})')
        return ('{self.__class__.__name__}('
                '{self.label!r}, {self.iri!r})'.format(self=self))
    
    def to_jsonld(self):
        return {'@id': self.iri,
                'label': self.label}
    
    @classmethod
    def from_jsonld(cls, data):
        if data is None:
            return None
        return cls(data["label"], data["@id"])


class Species(OntologyTerm):
    """docstring"""
    iri_map = {
        "Mus musculus": "http://purl.obolibrary.org/obo/NCBITaxon_10090"
    }


class Strain(OntologyTerm):
    """docstring"""
    iri_map = {
        "Tg2576": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "C57BL/6": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "C57BL/6": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "C57BL/6J X SJL": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "C57BL/6J": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567"
    }


class Sex(OntologyTerm):
    """docstring"""
    iri_map = {
        "male": "schema:Male",
        "female": "schema:Female"
    }


class BrainRegion(OntologyTerm):
    """docstring"""
    iri_map = {
        "hippocampus CA1": "http://purl.obolibrary.org/obo/UBERON_0003881",
        "hippocampus": "http://purl.obolibrary.org/obo/UBERON_0001954",
        "ventral hippocampus": "http://purl.obolibrary.org/obo/UBERON_0001954",   # how to distinguish this? Question for Tier 2 folks?
    }

class CellType(OntologyTerm):
    """docstring"""
    iri_map = {
        "hippocampus CA1 pyramidal cell": "http://uri.neuinfo.org/nif/nifstd/sao830368389",
    }


class QuantitativeValue(object):
    """docstring"""
    unit_codes = {
        "days": "http://purl.obolibrary.org/obo/UO_0000033",
        "months": "http://purl.obolibrary.org/obo/UO_0000035",
        "degrees": "http://purl.obolibrary.org/obo/UO_0000185",
        "µm": "http://purl.obolibrary.org/obo/UO_0000017",
        "mV":  "http://purl.obolibrary.org/obo/UO_0000247",
        "ms": "http://purl.obolibrary.org/obo/UO_0000028",
    }

    def __init__(self, value, unit_text, unit_code=None):
        self.value = value
        self.unit_text = unit_text
        self.unit_code = unit_code or self.unit_codes[unit_text]

    def __repr__(self):
        #return (f'{self.__class__.__name__}('
        #        f'{self.value!r} {self.unit_text!r})')
        return ('{self.__class__.__name__}('
                '{self.value!r} {self.unit_text!r})'.format(self=self))

    def to_jsonld(self):
        return {
            "@type": "nsg:QuantitativeValue",  # needs 'nsg:' prefix, no?
            "value": self.value,
            "label": self.unit_text,
            "unitCode": {"@id": self.unit_code}
        }
    
    def to_jsonld_alt(self):
        return {
            "value": self.value,
            "unitText": self.unit_text
        }

    @classmethod
    def from_jsonld(cls, data):
        if data is None:
            return None
        if "label" in data:
            unit_text = data["label"]
        elif "unitText" in data:
            unit_text = data["unitText"]
        else:
            unit_text = "?"
        if "unitCode" in data:
            unit_code = data["unitCode"]["@id"]
        else:
            unit_code = None
        return cls(data["value"], unit_text, unit_code)


class Age(object):

    def __init__(self, value, period):
        self.value = value
        self.period = period

    def __repr__(self):
        #return (f'{self.__class__.__name__}('
        #        f'{self.value!r}, {self.period!r})')
        return ('{self.__class__.__name__}('
                '{self.value!r}, {self.period!r})'.format(self=self))

    def to_jsonld(self):
        return {'value': self.value.to_jsonld(),
                'period': self.period}
    
    @classmethod
    def from_jsonld(cls, data):
        if data is None:
            return None
        return cls(QuantitativeValue.from_jsonld(data["value"]), data["period"])
