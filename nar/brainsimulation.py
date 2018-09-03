"""
brain simulation
"""

from .base import KGObject, cache  # KGProxy, KGQuery, lookup
# from .commons import QuantitativeValue, BrainRegion, CellType
# from .core import Subject, Person
# from .minds import Dataset


NAMESPACE = "neuralactivity"
# NAMESPACE = "neurosciencegraph"
# NAMESPACE = "brainsimulation"


class ModelProject(KGObject):
    """docstring"""
    path = NAMESPACE + "neuralactivity/simulation/modelproject/v0.1.0"
    type = ["prov:Entity", "nsg:ModelProject"]

    context = {
        "name": "schema:name",
        "alias": "nsg:alias",
        "author": "schema:author",
        "owner": "nsg:owner",
        "organization": "nsg:organization",
        "PLAComponents": "nsg:PLAComponents",
        "private": "nsg:private",
        "collabID": "nsg:collabID",
        "brainRegion": "nsg:brainRegion",
        "species": "nsg:species",
        "celltype": "nsg:celltype",
        "abstractionLevel": "nsg:abstractionLevel",
        "modelOf": "nsg:modelOf",
        "description": "schema:description",
        "nsg": "https://bbp-nexus.epfl.ch/vocabs/bbp/neurosciencegraph/core/v0.1.0/",
        "prov": "http://www.w3.org/ns/prov#",
        "schema": "http://schema.org/",
        "dateCreated": "schema:dateCreated",
    }

    def __init__(self, name, alias, author, owner, organization, pla_components, private, collab_id, brain_region,
                 species, celltype, abstraction_level, description, date_created, model_of=None):
        self.name = name
        self.alias = alias
        self.brain_region = brain_region
        self.species = species
        self.celltype = celltype
        self.organization = organization
        self.abstraction_level = abstraction_level
        self.private = private
        self.author = author
        self.owner = owner
        self.description = description
        self.collab_id = collab_id
        self.PLA_components = pla_components
        self.date_created = date_created
        self.model_of = model_of

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r}, {self.owner!r}, '
                '{self.date_created!r})'.format(self=self))

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        pass
        """
        D = instance.data
        assert 'nsg:ModelProject' in D["@type"]
        #  # todo: handle qualifiedGeneration
        if "modelOf" in D:
            model_of = KGProxy(Dataset, D["modelOf"]["@id"])
        else:
            model_of = None
        return cls(D["name"], D["distribution"],
                   KGProxy(PatchClampExperiment, D["wasGeneratedBy"]["@id"]),
                   KGProxy(QualifiedGeneration, D["qualifiedGeneration"]["@id"]),
                   D["channel"], D["dataUnit"],
                   QuantitativeValue.from_jsonld(D["timeStep"]),
                   model_of=model_of,
                   id=D["@id"], instance=instance)
        """

    def save(self, client, exists_ok=True):
        pass
        """
        if self.instance:
            data = self.instance.data
        else:
            data = {
                "@context": self.context,
                "@type": self.type
            }
        data["name"] = self.name
        data["distribution"] = self.data_location
        data["wasGeneratedBy"] = {
            "@type": self.generated_by.type,
            "@id": self.generated_by.id
        }
        data["qualifiedGeneration"] = {
            "@type": self.generation_metadata.type,
            "@id": self.generation_metadata.id
        }
        if self.channel is not None:  # could be 0, which is a valid value, but falsy
            data["channel"] = self.channel
        if self.data_unit:
            data["dataUnit"] = self.data_unit
        if self.time_step:
            data["timeStep"] = self.time_step.to_jsonld_alt()
        if self.model_of:
            data["partOf"] = {
                "@type": self.model_of.type,
                "@id": self.model_of.id
            }
        self._save(data, client, exists_ok)
        """

