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
        "Rodentia": "http://purl.obolibrary.org/obo/NCBITaxon_9989",
        "Mus musculus": "http://purl.obolibrary.org/obo/NCBITaxon_10090",
        "Rattus norvegicus": "http://purl.obolibrary.org/obo/NCBITaxon_10116",
        "Callithrix jacchus": "http://purl.obolibrary.org/obo/NCBITaxon_9483",
        "Homo sapiens": "http://purl.obolibrary.org/obo/NCBITaxon_9606",
        "Macaca mulatta": "http://purl.obolibrary.org/obo/NCBITaxon_9544",
        "Monodelphis domestica": "http://purl.obolibrary.org/obo/NCBITaxon_13616"
    }


class Strain(OntologyTerm):
    """docstring"""
    iri_map = {
        "Tg2576": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "C57BL/6": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "C57BL/6J X SJL": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "C57BL/6J": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "Sprague-Dawley": "https://rgd.mcw.edu/rgdweb/report/strain/main.html?id=70508"
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
        "somatosensory cortex": "http://purl.obolibrary.org/obo/UBERON_0008930",
        "thalamus": "http://purl.obolibrary.org/obo/UBERON_0001897",
        "brainstem": "http://purl.obolibrary.org/obo/UBERON_0002298",
        "spinal cord": "http://purl.obolibrary.org/obo/UBERON_0002240",
        "basal ganglia": "http://purl.obolibrary.org/obo/UBERON_0010011",
        "cortex": "http://purl.obolibrary.org/obo/UBERON_0001851",
        "cerebellum": "http://purl.obolibrary.org/obo/UBERON_0002037",
        "whole brain": "http://purl.obolibrary.org/obo/UBERON_0000955",
        "striatum": "http://purl.obolibrary.org/obo/UBERON_0002435",
        "thalamocortical": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "other": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
    }


class CellType(OntologyTerm):
    """docstring"""
    iri_map = {
        "hippocampus CA1 pyramidal cell": "http://uri.neuinfo.org/nif/nifstd/sao830368389",
        "hippocampus CA1 basket cell": "http://uri.neuinfo.org/nif/nifstd/nlx_cell_091205",
        "hippocampus interneuron BP": "unknown",
        "hippocampus CA1 bistratified cell": "unknown",
        "hippocampus CA1 lacunosum moleculare neuron": "http://uri.neuinfo.org/nif/nifstd/nlx_92500",
        "hippocampus CA1 ivy neuron": "http://uri.neuinfo.org/nif/nifstd/nlx_35220",
        "Purkinje cell": "http://purl.obolibrary.org/obo/CL_0000121",
        "medium spiny neuron": "http://purl.obolibrary.org/obo/CL_1001474",
        "interneuron": "http://purl.obolibrary.org/obo/CL_0000099",
        "golgi cell": "http://purl.obolibrary.org/obo/CL_0000119",
        "pyramidal cell": "http://purl.obolibrary.org/obo/CL_0000598",
        "granule cell": "http://purl.obolibrary.org/obo/CL_0000120",
        "L2/3 chandelier cell": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "fast spiking interneuron": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "spiny stellate neuron": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "L5 tufted pyramidal cell": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "L2/3 pyramidal cell": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "medium spiny neuron (D2 type)": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "L6 inverted pyramidal cell": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "L4 martinotti cell": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "medium spiny neuron (D1 type)": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "cholinergic interneuron": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "L1 neurogliaform cell": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "L2 inverted pyramidal cell": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "not applicable": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "other": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
    }


class AbstractionLevel(OntologyTerm):
    """docstring"""
    iri_map = {
        "Protein structure": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "Systems biology": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "_continuous": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "_discrete": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "_flux balance": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "Spiking neurons": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "_biophysical": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "_point neuron": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "Rate neurons": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "Population modelling": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "_neural field": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "_neural mass": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "Cognitive modelling": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "Other - please specify": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
    }


class QuantitativeValue(object):
    """docstring"""
    unit_codes = {
        "days": "http://purl.obolibrary.org/obo/UO_0000033",
        "weeks": "http://purl.obolibrary.org/obo/UO_0000034",
        "months": "http://purl.obolibrary.org/obo/UO_0000035",
        "degrees": "http://purl.obolibrary.org/obo/UO_0000185",
        "µm": "http://purl.obolibrary.org/obo/UO_0000017",
        "mV":  "http://purl.obolibrary.org/obo/UO_0000247",
        "ms": "http://purl.obolibrary.org/obo/UO_0000028",
    }

    def __init__(self, value, unit_text, unit_code=None):
        if not isinstance(value, (int, float)):
            raise ValueError("Must be a number")
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
        return cls(float(data["value"]), unit_text, unit_code)


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
