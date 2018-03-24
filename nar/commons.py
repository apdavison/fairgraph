"""

"""

from typing import NamedTuple


class Address(NamedTuple):
    locality: str
    country: str

# for Python 2, could use Address = collections.namedtuple('Employee', ['locality', 'country'])

class OntologyTerm(object):
    """docstring"""

    def __init__(self, label, iri=None):
        self.label = label
        self.iri = iri or self.iri_map[label]

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.label!r}, {self.iri!r})')
    
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
        return (f'{self.__class__.__name__}('
                f'{self.value!r} {self.unit_text!r})')
    
    def to_jsonld(self):
        return {
            "@type": "QuantitativeValue",
            "value": self.value,
            "label": self.unit_text,
            "unitCode": {"@id": self.unit_code}
        }
    
    @classmethod
    def from_jsonld(cls, data):
        if data is None:
            return None
        return cls(data["value"], data["label"], data["unitCode"]["@id"])


class Age(object):

    def __init__(self, value, period):
        self.value = value
        self.period = period

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.value!r}, {self.period!r})')
    
    def to_jsonld(self):
        return {'value': self.value.to_jsonld(),
                'period': self.period}
    
    @classmethod
    def from_jsonld(cls, data):
        if data is None:
            return None
        return cls(QuantitativeValue.from_jsonld(data["value"]), data["period"])
