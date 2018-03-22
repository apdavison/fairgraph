"""

"""

from typing import NamedTuple


class Address(NamedTuple):
    locality: str
    country: str

# for Python 2, could use Address = collections.namedtuple('Employee', ['locality', 'country'])

class OntologyTerm(object):
    """docstring"""

    def __init__(self, label, iri):
        self.label = label
        self.iri = iri

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
    pass


class Strain(OntologyTerm):
    """docstring"""
    pass

class Sex(OntologyTerm):
    """docstring"""
    pass


class QuantitativeValue(object):
    def __init__(self, value, unit_text, unit_code):
        self.value = value
        self.unit_text = unit_text
        self.unit_code = unit_code

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.value!r} {self.unit_text!r})')
    
    def to_jsonld(self):
        return {'value': self.value,
                'label': self.unit_text,
                'unitCode': {'@id': self.unit_code}}
    
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
