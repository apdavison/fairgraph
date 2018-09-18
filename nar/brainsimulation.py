"""
brain simulation
"""

from .base import KGObject, cache, KGProxy
from .commons import BrainRegion, CellType, Species, AbstractionLevel
from .core import Organization, Person
import datetime


NAMESPACE = "neuralactivity"


class ModelProject(KGObject):
    """docstring"""
    path = NAMESPACE + "/simulation/modelproject/v0.1.0"
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

    def __init__(self, name, owner, author, description, date_created, private, collab_id, alias=None,
                 organization=None, pla_components=None, brain_region=None, species=None, celltype=None,
                 abstraction_level=None, model_of=None, id=None, instance=None):
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
        self.id = id
        self.instance = instance

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r}, {self.owner!r}, '
                '{self.date_created!r}, {self.id})'.format(self=self))

    @classmethod
    @cache
    def from_kg_instance(cls, instance, client):
        D = instance.data
        assert 'nsg:ModelProject' in D["@type"]
        return cls(name=D["name"], owner=KGProxy(Person, D["owner"]), author=KGProxy(Person, D["author"]),
                   collab_id=D["collabID"], description=D["description"], private=D["private"],
                   date_created=D["dateCreated"], organization=KGProxy(Organization, D.get("organization", None)),
                   pla_components=D.get("PLAComponents", None), alias=D.get("alias", None),
                   model_of=D.get("modelOf", None), brain_region=BrainRegion.from_jsonld(D.get("brainRegion", None)),
                   species=Species.from_jsonld(D.get("species", None)),
                   celltype=CellType.from_jsonld(D.get("celltype", None)),
                   abstraction_level=AbstractionLevel.from_jsonld(D.get("abstractionLevel", None)),
                   id=D["@id"], instance=instance)

    def save(self, client, exists_ok=True):
        if self.instance:
            data = self.instance.data
        else:
            data = {
                "@context": self.context,
                "@type": self.type
            }
        if self.author:
            if self.author.id is None:
                self.author.save(client)
            data["author"] = {
                "@type": self.author.type,
                "@id": self.author.id
            }
        if self.owner:
            if self.owner.id is None:
                self.owner.save(client)
            data["owner"] = {
                "@type": self.owner.type,
                "@id": self.owner.id
            }
        data["name"] = self.name
        data["collabID"] = self.collab_id
        data["description"] = self.description
        data["private"] = self.private
        if type(self.date_created) is datetime.date or type(self.date_created) is datetime.datetime:
            data["dateCreated"] = self.date_created.strftime("%d/%m/%y, %I:%M")
        else:
            data["dateCreated"] = self.date_created
        if self.organization is not None:
            if self.organization.id is None:
                self.organization.save(client)
            data["organization"] = {
                "@type": self.organization.type,
                "@id": self.organization.id
            }
        if self.PLA_components is not None:
            data["PLAComponents"] = self.PLA_components
        if self.alias is not None:
            data["alias"] = self.alias
        if self.model_of is not None:
            data["modelOf"] = self.model_of
        if self.brain_region is not None:
            data["brainRegion"] = self.brain_region.to_jsonld()
        if self.species is not None:
            data["species"] = self.species.to_jsonld()
        if self.celltype is not None:
            data["celltype"] = self.celltype.to_jsonld()
        if self.abstraction_level is not None:
            data["abstractionLevel"] = self.abstraction_level.to_jsonld()
        self._save(data, client, exists_ok)
