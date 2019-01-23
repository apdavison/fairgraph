# encoding: utf-8
"""

"""

import collections
#from typing import NamedTuple
from .base import KGObject, KGProxy, OntologyTerm


#class Address(NamedTuple):
#    locality: str
#    country: str

Address = collections.namedtuple('Address', ['locality', 'country'])


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
        #"Sprague-Dawley": "https://rgd.mcw.edu/rgdweb/report/strain/main.html?id=70508",
        "Sprague-Dawley": "https://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=RS:0000681",
        #"Wistar":  "https://rgd.mcw.edu/rgdweb/report/strain/main.html?id=13508588",
        "Wistar": "https://rgd.mcw.edu/rgdweb/ontology/view.html?acc_id=RS:0001013",
        "129/Sv": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        # 129/Sv is ambiguous
        # could be https://www.jax.org/strain/002448 or https://www.jax.org/strain/000691 or other
        # see http://www.informatics.jax.org/mgihome/nomen/strain_129.shtml
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
        "5th cerebellar lobule": "http://purl.obolibrary.org/obo/UBERON_0004004",  
        # more specific term to be determined: http://purl.obolibrary.org/obo/UBERON_0024001 or http://purl.obolibrary.org/obo/UBERON_0004079 ?
        "6th cerebellar lobule": "http://purl.obolibrary.org/obo/UBERON_0004004",  # more specific term to be determined
        "7th cerebellar lobule": "http://purl.obolibrary.org/obo/UBERON_0004004",  # more specific term to be determined
        "8th cerebellar lobule": "http://purl.obolibrary.org/obo/UBERON_0004004",  # more specific term to be determined
        "lobule 5 of the cerebellar vermis": "http://purl.obolibrary.org/obo/UBERON_0004079",
        "lobule 6 of the cerebellar vermis": "http://purl.obolibrary.org/obo/UBERON_0004080",
        "lobule 7 of the cerebellar vermis": "http://purl.obolibrary.org/obo/UBERON_0004081",
        "lobule 8 of the cerebellar vermis": "http://purl.obolibrary.org/obo/UBERON_0004082",
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
        "Golgi cell": "http://purl.obolibrary.org/obo/CL_0000119",
        "pyramidal cell": "http://purl.obolibrary.org/obo/CL_0000598",
        "granule cell": "http://purl.obolibrary.org/obo/CL_0000120",
        "L2/3 chandelier cell": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "fast spiking interneuron": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "spiny stellate neuron": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "L5 tufted pyramidal cell": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "L2/3 pyramidal cell": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "medium spiny neuron (D2 type)": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "L6 inverted pyramidal cell": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "L4 Martinotti cell": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "medium spiny neuron (D1 type)": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "cholinergic interneuron": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "L1 neurogliaform cell": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "L2 inverted pyramidal cell": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "not applicable": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567"
    }


class AbstractionLevel(OntologyTerm):
    """docstring"""
    iri_map = {
        "protein structure": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "systems biology": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "systems biology: continuous": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "systems biology: discrete": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "systems biology: flux balance": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "spiking neurons": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "spiking neurons: biophysical": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "spiking neurons: point neuron": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "rate neurons": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "population modelling": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "population modelling: neural field": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "population modelling: neural mass": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567",
        "cognitive modelling": "http://www.hbp.FIXME.org/hbp_taxonomy_ontology/1234567"
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
