

from .minds import MINDSObject

DEFAULT_NAMESPACE = "uniminds"

# options
"https://kg.humanbrainproject.org/query/uniminds/options/abstractionlevel/v1.0.0/abstractionLevel/instances"


class ModelRelease(MINDSObject):
    """docstring"""
    namespace = DEFAULT_NAMESPACE
    _path = "/core/modelinstance/v1.0.0"
    type = ["uniminds:Modelinstance"]
    property_names = ["identifier", "name", "description", "version",
                      "abstractionLevel", "brainStructure", "cellularTarget",
                      "contributor", "custodian", "mainContact", "modelFormat",
                      "modelScope", "publication", "studyTarget"]  #, "license"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} @ {self.version!r} {self.id!r})'.format(self=self))


class FileBundle(MINDSObject):
    """docstring"""
    namespace = DEFAULT_NAMESPACE
    _path = "/core/filebundle/v1.0.0"
    type = ["uniminds:FileBundle"]
    property_names = ["identifier", "name", "description", "url", "usageNotes", "modelInstance"]

    def __repr__(self):
        return ('{self.__class__.__name__}('
                '{self.name!r} {self.url!r} {self.id!r})'.format(self=self))


class Person(MINDSObject):
    """docstring"""
    namespace = DEFAULT_NAMESPACE
    _path = "/core/person/v1.0.0"
    type = ["uniminds:Person"]
    property_names = ["name", "familyName", "givenName", "email", "identifier"] # "orcid"

    @property
    def full_name(self):
        return '{self.givenName} {self.familyName}'.format(self=self)

    @property
    def _existence_query(self):
        return {
            "op": "and",
            "value": [
                {
                    "path": "schema:familyName",
                    "op": "eq",
                    "value": self.familyName
                },
                {
                    "path": "schema:givenName",
                    "op": "eq",
                    "value": self.givenName
                }
            ]
        }


class UniMINDSOption():
    pass

#     Abstraction level
# Age category
# Brain structure
# Cellular target
# Country
# DOI
# Disability/disease
# Embargo status
# Ethics authority
# Experimental preparation
# File bundle group
# Genotype
# Handedness
# License
# MIME type
# Method category
# Model format
# Model scope
# Organ
# Organization
# Pathology
# Publication id type
# PublicationId
# Sex
# Species
# Strain
# Study target source
# Study target type
# Tissue sample piece