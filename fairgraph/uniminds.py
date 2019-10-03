import sys, inspect
from datetime import datetime
from tabulate import tabulate
from fairgraph.base import KGObject, KGProxy, KGQuery, cache, as_list, Field
from fairgraph.data import FileAssociation, CSCSFile
from fairgraph.commons import QuantitativeValue

try:
    from .minds import MINDSObject, basestring
except ModuleNotFoundError:
    from minds import MINDSObject, basestring

    
class Abstractionlevel(MINDSObject):
    """
    docstring
    """
    _path = "/options/abstractionlevel/v1.0.0"
    type = ["uniminds:Abstractionlevel"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("abstraction_level", "AbstractionLevel", "https://schema.hbp.eu/uniminds/abstractionLevel", required=False, multiple=False))
    


class AgeCategory(MINDSObject):
    """
    docstring
    """
    _path = "/options/agecategory/v1.0.0"
    type = ["uniminds:AgeCategory"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("age_category", "AgeCategory", "https://schema.hbp.eu/uniminds/ageCategory", required=False, multiple=False))
    


class BrainStructure(MINDSObject):
    """
    docstring
    """
    _path = "/options/brainstructure/v1.0.0"
    type = ["uniminds:BrainStructure"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("brain_structure", "BrainStructure", "https://schema.hbp.eu/uniminds/brainStructure", required=False, multiple=False))
    


class CellularTarget(MINDSObject):
    """
    docstring
    """
    _path = "/options/cellulartarget/v1.0.0"
    type = ["uniminds:CellularTarget"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("cellular_target", "CellularTarget", "https://schema.hbp.eu/uniminds/cellularTarget", required=False, multiple=False))
    


class Country(MINDSObject):
    """
    docstring
    """
    _path = "/options/country/v1.0.0"
    type = ["uniminds:Country"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("country_of_origin", "Country", "https://schema.hbp.eu/uniminds/countryOfOrigin", required=False, multiple=False))
    


class Dataset(MINDSObject):
    """
    docstring
    """
    _path = "/core/dataset/v1.0.0"
    type = ["uniminds:Dataset"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("description", basestring, "http://schema.org/description", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("intended_release_date", datetime, "https://schema.hbp.eu/uniminds/intendedReleaseDate", required=False, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("brain_structure", "BrainStructure", "https://schema.hbp.eu/uniminds/brainStructure", required=False, multiple=False),
      Field("cellular_target", "CellularTarget", "https://schema.hbp.eu/uniminds/cellularTarget", required=False, multiple=False),
      Field("contributor", "Person", "https://schema.hbp.eu/uniminds/contributor", required=False, multiple=True),
      Field("created_as", basestring, "https://schema.hbp.eu/uniminds/createdAs", required=False, multiple=False),
      Field("custodian", "Person", "https://schema.hbp.eu/uniminds/custodian", required=False, multiple=False),
      Field("doi", "Doi", "https://schema.hbp.eu/uniminds/doi", required=False, multiple=False),
      Field("embargo_status", "EmbargoStatus", "https://schema.hbp.eu/uniminds/embargoStatus", required=False, multiple=False),
      Field("ethics_approval", "EthicsApproval", "https://schema.hbp.eu/uniminds/ethicsApproval", required=False, multiple=False),
      Field("funding_information", "FundingInformation", "https://schema.hbp.eu/uniminds/fundingInformation", required=False, multiple=False),
      Field("hbp_component", "HbpComponent", "https://schema.hbp.eu/uniminds/hbpComponent", required=False, multiple=False),
      Field("license", "License", "https://schema.hbp.eu/uniminds/license", required=False, multiple=False),
      Field("main_contact", "Person", "https://schema.hbp.eu/uniminds/mainContact", required=False, multiple=False),
      Field("main_file_bundle", basestring, "https://schema.hbp.eu/uniminds/mainFileBundle", required=False, multiple=False),
      Field("method", "Method", "https://schema.hbp.eu/uniminds/method", required=False, multiple=False),
      Field("project", "Project", "https://schema.hbp.eu/uniminds/project", required=False, multiple=False),
      Field("publication", "Publication", "https://schema.hbp.eu/uniminds/publication", required=False, multiple=False),
      Field("species", "Species", "https://schema.hbp.eu/uniminds/species", required=False, multiple=False),
      Field("study_target", "StudyTarget", "https://schema.hbp.eu/uniminds/studyTarget", required=False, multiple=False),
      Field("subjectgroup", "SubjectGroup", "https://schema.hbp.eu/uniminds/subjectGroup", required=False, multiple=False))
    


class Disability(MINDSObject):
    """
    docstring
    """
    _path = "/options/disability/v1.0.0"
    type = ["uniminds:Disability"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("disability", "Disability", "https://schema.hbp.eu/uniminds/disability", required=False, multiple=False))
    


class Doi(MINDSObject):
    """
    docstring
    """
    _path = "/options/doi/v1.0.0"
    type = ["uniminds:Doi"]
    fields = (
      Field("citation", basestring, "https://schema.hbp.eu/uniminds/citation", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("doi", "Doi", "https://schema.hbp.eu/uniminds/doi", required=False, multiple=False))
    


class EmbargoStatus(MINDSObject):
    """
    docstring
    """
    _path = "/options/embargostatus/v1.0.0"
    type = ["uniminds:EmbargoStatus"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("embargo_status", "EmbargoStatus", "https://schema.hbp.eu/uniminds/embargoStatus", required=False, multiple=False))
    


class EthicsApproval(MINDSObject):
    """
    docstring
    """
    _path = "/core/ethicsapproval/v1.0.0"
    type = ["uniminds:EthicsApproval"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("hbpethicsapproval", basestring, "https://schema.hbp.eu/uniminds/hbpEthicsApproval", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("country_of_origin", "Country", "https://schema.hbp.eu/uniminds/countryOfOrigin", required=False, multiple=False),
      Field("ethics_approval", "EthicsApproval", "https://schema.hbp.eu/uniminds/ethicsApproval", required=False, multiple=False),
      Field("ethics_authority", "EthicsAuthority", "https://schema.hbp.eu/uniminds/ethicsAuthority", required=False, multiple=False))
    


class EthicsAuthority(MINDSObject):
    """
    docstring
    """
    _path = "/options/ethicsauthority/v1.0.0"
    type = ["uniminds:EthicsAuthority"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("ethics_authority", "EthicsAuthority", "https://schema.hbp.eu/uniminds/ethicsAuthority", required=False, multiple=False))
    


class ExperimentalPreparation(MINDSObject):
    """
    docstring
    """
    _path = "/options/experimentalpreparation/v1.0.0"
    type = ["uniminds:ExperimentalPreparation"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("experimental_preparation", "ExperimentalPreparation", "https://schema.hbp.eu/uniminds/experimentalPreparation", required=False, multiple=False))
    


class File(MINDSObject):
    """
    docstring
    """
    _path = "/core/file/v1.0.0"
    type = ["uniminds:File"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("description", basestring, "http://schema.org/description", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("url", basestring, "http://schema.org/url", required=False, multiple=False),
      Field("brain_structure", "BrainStructure", "https://schema.hbp.eu/uniminds/brainStructure", required=False, multiple=False),
      Field("file", "File", "https://schema.hbp.eu/uniminds/file", required=False, multiple=False),
      Field("method", "Method", "https://schema.hbp.eu/uniminds/method", required=False, multiple=False),
      Field("mime_type", "MimeType", "https://schema.hbp.eu/uniminds/mimeType", required=False, multiple=False),
      Field("study_target", "StudyTarget", "https://schema.hbp.eu/uniminds/studyTarget", required=False, multiple=False),
      Field("subject", "Subject", "https://schema.hbp.eu/uniminds/subject", required=False, multiple=False),
      Field("subjectgroup", "SubjectGroup", "https://schema.hbp.eu/uniminds/subjectGroup", required=False, multiple=False))
    


class FileAssociation(MINDSObject):
    """
    docstring
    """
    _path = "/core/fileassociation/v1.0.0"
    type = ["uniminds:FileAssociation"]
    fields = (
      Field("from", basestring, "https://schema.hbp.eu/linkinginstance/from", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("to", basestring, "https://schema.hbp.eu/linkinginstance/to", required=False, multiple=False))
    


class FileBundle(MINDSObject):
    """
    docstring
    """
    _path = "/core/filebundle/v1.0.0"
    type = ["uniminds:FileBundle"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("description", basestring, "http://schema.org/description", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("url", basestring, "http://schema.org/url", required=False, multiple=False),
      Field("usage_notes", basestring, "https://schema.hbp.eu/uniminds/usageNotes", required=False, multiple=False),
      Field("brain_structure", "BrainStructure", "https://schema.hbp.eu/uniminds/brainStructure", required=False, multiple=False),
      Field("cellular_target", "CellularTarget", "https://schema.hbp.eu/uniminds/cellularTarget", required=False, multiple=False),
      Field("file", "File", "https://schema.hbp.eu/uniminds/file", required=False, multiple=False),
      Field("file_bundle", "FileBundle", "https://schema.hbp.eu/uniminds/fileBundle", required=False, multiple=False),
      Field("main_file_bundle", basestring, "https://schema.hbp.eu/uniminds/mainFileBundle", required=False, multiple=False),
      Field("method", "Method", "https://schema.hbp.eu/uniminds/method", required=False, multiple=False),
      Field("mime_type", "MimeType", "https://schema.hbp.eu/uniminds/mimeType", required=False, multiple=False),
      Field("model_instance", "ModelInstance", "https://schema.hbp.eu/uniminds/modelInstance", required=False, multiple=False),
      Field("publication", "Publication", "https://schema.hbp.eu/uniminds/publication", required=False, multiple=False),
      Field("study_target", "StudyTarget", "https://schema.hbp.eu/uniminds/studyTarget", required=False, multiple=False),
      Field("subject", "Subject", "https://schema.hbp.eu/uniminds/subject", required=False, multiple=False),
      Field("subjectgroup", "SubjectGroup", "https://schema.hbp.eu/uniminds/subjectGroup", required=False, multiple=False))
    


class FileBundleGroup(MINDSObject):
    """
    docstring
    """
    _path = "/options/filebundlegroup/v1.0.0"
    type = ["uniminds:FileBundleGroup"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False))
    


class FundingInformation(MINDSObject):
    """
    docstring
    """
    _path = "/core/fundinginformation/v1.0.0"
    type = ["uniminds:FundingInformation"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("grant_id", basestring, "https://schema.hbp.eu/uniminds/grantId", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("funding_information", "FundingInformation", "https://schema.hbp.eu/uniminds/fundingInformation", required=False, multiple=False))
    


class Genotype(MINDSObject):
    """
    docstring
    """
    _path = "/options/genotype/v1.0.0"
    type = ["uniminds:Genotype"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("genotype", "Genotype", "https://schema.hbp.eu/uniminds/genotype", required=False, multiple=False))
    


class Handedness(MINDSObject):
    """
    docstring
    """
    _path = "/options/handedness/v1.0.0"
    type = ["uniminds:Handedness"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("handedness", "Handedness", "https://schema.hbp.eu/uniminds/handedness", required=False, multiple=False))
    


class HbpComponent(MINDSObject):
    """
    docstring
    """
    _path = "/core/hbpcomponent/v1.0.0"
    type = ["uniminds:HbpComponent"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("associated_task", basestring, "https://schema.hbp.eu/uniminds/associatedTask", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("component_owner", basestring, "https://schema.hbp.eu/uniminds/componentOwner", required=False, multiple=False),
      Field("hbp_component", "HbpComponent", "https://schema.hbp.eu/uniminds/hbpComponent", required=False, multiple=False))
    


class License(MINDSObject):
    """
    docstring
    """
    _path = "/options/license/v1.0.0"
    type = ["uniminds:License"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("fullname", basestring, "https://schema.hbp.eu/uniminds/fullName", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("url", basestring, "http://schema.org/url", required=False, multiple=False),
      Field("license", "License", "https://schema.hbp.eu/uniminds/license", required=False, multiple=False))
    


class Method(MINDSObject):
    """
    docstring
    """
    _path = "/core/method/v1.0.0"
    type = ["uniminds:Method"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("description", basestring, "http://schema.org/description", required=False, multiple=False),
      Field("fullname", basestring, "https://schema.hbp.eu/uniminds/fullName", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("brain_structure", "BrainStructure", "https://schema.hbp.eu/uniminds/brainStructure", required=False, multiple=False),
      Field("ethics_approval", "EthicsApproval", "https://schema.hbp.eu/uniminds/ethicsApproval", required=False, multiple=False),
      Field("experimental_preparation", "ExperimentalPreparation", "https://schema.hbp.eu/uniminds/experimentalPreparation", required=False, multiple=False),
      Field("method", "Method", "https://schema.hbp.eu/uniminds/method", required=False, multiple=False),
      Field("method_category", "MethodCategory", "https://schema.hbp.eu/uniminds/methodCategory", required=False, multiple=False),
      Field("publication", "Publication", "https://schema.hbp.eu/uniminds/publication", required=False, multiple=False),
      Field("study_target", "StudyTarget", "https://schema.hbp.eu/uniminds/studyTarget", required=False, multiple=False),
      Field("submethod", basestring, "https://schema.hbp.eu/uniminds/subMethod", required=False, multiple=False))
    


class MethodCategory(MINDSObject):
    """
    docstring
    """
    _path = "/options/methodcategory/v1.0.0"
    type = ["uniminds:MethodCategory"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("method_category", "MethodCategory", "https://schema.hbp.eu/uniminds/methodCategory", required=False, multiple=False))
    


class MimeType(MINDSObject):
    """
    docstring
    """
    _path = "/options/mimetype/v1.0.0"
    type = ["uniminds:MimeType"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("mime_type", "MimeType", "https://schema.hbp.eu/uniminds/mimeType", required=False, multiple=False))
    


class ModelFormat(MINDSObject):
    """
    docstring
    """
    _path = "/options/modelformat/v1.0.0"
    type = ["uniminds:ModelFormat"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("modelformat", "ModelFormat", "https://schema.hbp.eu/uniminds/modelFormat", required=False, multiple=False))
    


class ModelInstance(MINDSObject):
    """
    docstring
    """
    _path = "/core/modelinstance/v1.0.0"
    type = ["uniminds:ModelInstance"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("description", basestring, "http://schema.org/description", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("license", "License", "http://schema.org/license", required=False, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("version", basestring, "http://schema.org/version", required=False, multiple=False),
      Field("abstraction_level", "AbstractionLevel", "https://schema.hbp.eu/uniminds/abstractionLevel", required=False, multiple=False),
      Field("brain_structure", "BrainStructure", "https://schema.hbp.eu/uniminds/brainStructure", required=False, multiple=False),
      Field("cellular_target", "CellularTarget", "https://schema.hbp.eu/uniminds/cellularTarget", required=False, multiple=False),
      Field("contributor", "Person", "https://schema.hbp.eu/uniminds/contributor", required=False, multiple=True),
      Field("custodian", "Person", "https://schema.hbp.eu/uniminds/custodian", required=False, multiple=False),
      Field("main_contact", "Person", "https://schema.hbp.eu/uniminds/mainContact", required=False, multiple=False),
      Field("modelformat", "ModelFormat", "https://schema.hbp.eu/uniminds/modelFormat", required=False, multiple=False),
      Field("model_instance", "ModelInstance", "https://schema.hbp.eu/uniminds/modelInstance", required=False, multiple=False),
      Field("modelscope", "ModelScope", "https://schema.hbp.eu/uniminds/modelScope", required=False, multiple=False),
      Field("publication", "Publication", "https://schema.hbp.eu/uniminds/publication", required=False, multiple=False),
      Field("study_target", "StudyTarget", "https://schema.hbp.eu/uniminds/studyTarget", required=False, multiple=False))
    


class ModelScope(MINDSObject):
    """
    docstring
    """
    _path = "/options/modelscope/v1.0.0"
    type = ["uniminds:ModelScope"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("modelscope", "ModelScope", "https://schema.hbp.eu/uniminds/modelScope", required=False, multiple=False))
    


class Organization(MINDSObject):
    """
    docstring
    """
    _path = "/options/organization/v1.0.0"
    type = ["uniminds:Organization"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("created_as", basestring, "https://schema.hbp.eu/uniminds/createdAs", required=False, multiple=False))
    


class Person(MINDSObject):
    """
    docstring
    """
    _path = "/core/person/v1.0.0"
    type = ["uniminds:Person"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("email", basestring, "http://schema.org/email", required=False, multiple=False),
      Field("family_name", basestring, "http://schema.org/familyName", required=False, multiple=False),
      Field("given_name", basestring, "http://schema.org/givenName", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("orcid", basestring, "https://schema.hbp.eu/uniminds/orcid", required=False, multiple=False),
      Field("component_owner", "Person", "https://schema.hbp.eu/uniminds/componentOwner", required=False, multiple=False),
      Field("contributor", "Person", "https://schema.hbp.eu/uniminds/contributor", required=False, multiple=True),
      Field("coordinator", "Person", "https://schema.hbp.eu/uniminds/coordinator", required=False, multiple=False),
      Field("custodian", "Person", "https://schema.hbp.eu/uniminds/custodian", required=False, multiple=False),
      Field("main_contact", "Person", "https://schema.hbp.eu/uniminds/mainContact", required=False, multiple=False))
    


class Project(MINDSObject):
    """
    docstring
    """
    _path = "/core/project/v1.0.0"
    type = ["uniminds:Project"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("description", basestring, "http://schema.org/description", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("coordinator", "Person", "https://schema.hbp.eu/uniminds/coordinator", required=False, multiple=False),
      Field("project", "Project", "https://schema.hbp.eu/uniminds/project", required=False, multiple=False))
    


class Publication(MINDSObject):
    """
    docstring
    """
    _path = "/core/publication/v1.0.0"
    type = ["uniminds:Publication"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("url", basestring, "http://schema.org/url", required=False, multiple=False),
      Field("brain_structure", "BrainStructure", "https://schema.hbp.eu/uniminds/brainStructure", required=False, multiple=False),
      Field("project", "Project", "https://schema.hbp.eu/uniminds/project", required=False, multiple=False),
      Field("publication", "Publication", "https://schema.hbp.eu/uniminds/publication", required=False, multiple=False),
      Field("publication_id", "PublicationId", "https://schema.hbp.eu/uniminds/publicationId", required=False, multiple=False),
      Field("study_target", "StudyTarget", "https://schema.hbp.eu/uniminds/studyTarget", required=False, multiple=False),
      Field("subjectgroup", "SubjectGroup", "https://schema.hbp.eu/uniminds/subjectGroup", required=False, multiple=False))
    


class PublicationId(MINDSObject):
    """
    docstring
    """
    _path = "/options/publicationid/v1.0.0"
    type = ["uniminds:PublicationId"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("publication", "Publication", "https://schema.hbp.eu/uniminds/publication", required=False, multiple=False),
      Field("publication_id", "PublicationId", "https://schema.hbp.eu/uniminds/publicationId", required=False, multiple=False),
      Field("publication_id_type", "PublicationIdType", "https://schema.hbp.eu/uniminds/publicationIdType", required=False, multiple=False))
    


class PublicationIdType(MINDSObject):
    """
    docstring
    """
    _path = "/options/publicationidtype/v1.0.0"
    type = ["uniminds:PublicationIdType"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("publication_id_type", "PublicationIdType", "https://schema.hbp.eu/uniminds/publicationIdType", required=False, multiple=False))
    


class Sex(MINDSObject):
    """
    docstring
    """
    _path = "/options/sex/v1.0.0"
    type = ["uniminds:Sex"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("sex", "Sex", "https://schema.hbp.eu/uniminds/sex", required=False, multiple=False))
    


class Species(MINDSObject):
    """
    docstring
    """
    _path = "/options/species/v1.0.0"
    type = ["uniminds:Species"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("species", "Species", "https://schema.hbp.eu/uniminds/species", required=False, multiple=False))
    


class Strain(MINDSObject):
    """
    docstring
    """
    _path = "/options/strain/v1.0.0"
    type = ["uniminds:Strain"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("strain", "Strain", "https://schema.hbp.eu/uniminds/strain", required=False, multiple=False))
    


class StudyTarget(MINDSObject):
    """
    docstring
    """
    _path = "/core/studytarget/v1.0.0"
    type = ["uniminds:StudyTarget"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("fullname", basestring, "https://schema.hbp.eu/uniminds/fullName", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("study_target", "StudyTarget", "https://schema.hbp.eu/uniminds/studyTarget", required=False, multiple=False),
      Field("study_target_source", "StudyTargetSource", "https://schema.hbp.eu/uniminds/studyTargetSource", required=False, multiple=False),
      Field("study_target_type", "StudyTargetType", "https://schema.hbp.eu/uniminds/studyTargetType", required=False, multiple=False))
    


class StudyTargetSource(MINDSObject):
    """
    docstring
    """
    _path = "/options/studytargetsource/v1.0.0"
    type = ["uniminds:StudyTargetSource"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False))
    


class StudyTargetType(MINDSObject):
    """
    docstring
    """
    _path = "/options/studytargettype/v1.0.0"
    type = ["uniminds:StudyTargetType"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False))
    


class Subject(MINDSObject):
    """
    docstring
    """
    _path = "/core/subject/v1.0.0"
    type = ["uniminds:Subject"]
    fields = (
      Field("age", QuantitativeValue, "https://schema.hbp.eu/uniminds/age", required=False, multiple=False),
      Field("age_rang_max", QuantitativeValue, "https://schema.hbp.eu/uniminds/ageRangeMax", required=False, multiple=False),
      Field("age_rang_min", QuantitativeValue, "https://schema.hbp.eu/uniminds/ageRangeMin", required=False, multiple=False),
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("age_category", "AgeCategory", "https://schema.hbp.eu/uniminds/ageCategory", required=False, multiple=False),
      Field("brain_structure", "BrainStructure", "https://schema.hbp.eu/uniminds/brainstructure", required=False, multiple=False),
      Field("cellular_target", "CellularTarget", "https://schema.hbp.eu/uniminds/cellularTarget", required=False, multiple=False),
      Field("disability", "Disability", "https://schema.hbp.eu/uniminds/disability", required=False, multiple=False),
      Field("genotype", "Genotype", "https://schema.hbp.eu/uniminds/genotype", required=False, multiple=False),
      Field("handedness", "Handedness", "https://schema.hbp.eu/uniminds/handedness", required=False, multiple=False),
      Field("method", "Method", "https://schema.hbp.eu/uniminds/method", required=False, multiple=False),
      Field("publication", "Publication", "https://schema.hbp.eu/uniminds/publication", required=False, multiple=False),
      Field("sex", "Sex", "https://schema.hbp.eu/uniminds/sex", required=False, multiple=False),
      Field("species", "Species", "https://schema.hbp.eu/uniminds/species", required=False, multiple=False),
      Field("strain", "Strain", "https://schema.hbp.eu/uniminds/strain", required=False, multiple=False),
      Field("study_target", "StudyTarget", "https://schema.hbp.eu/uniminds/studyTarget", required=False, multiple=False),
      Field("subject", "Subject", "https://schema.hbp.eu/uniminds/subject", required=False, multiple=False),
      Field("subjects", "Subject", "https://schema.hbp.eu/uniminds/subjects", required=False, multiple=True))
    


class SubjectGroup(MINDSObject):
    """
    docstring
    """
    _path = "/core/subjectgroup/v1.0.0"
    type = ["uniminds:SubjectGroup"]
    fields = (
      Field("age_rang_max", QuantitativeValue, "https://schema.hbp.eu/uniminds/ageRangeMax", required=False, multiple=False),
      Field("age_rang_min", QuantitativeValue, "https://schema.hbp.eu/uniminds/ageRangeMin", required=False, multiple=False),
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("description", basestring, "http://schema.org/description", required=False, multiple=False),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("num_of_subjects", QuantitativeValue, "https://schema.hbp.eu/uniminds/numOfSubjects", required=False, multiple=False),
      Field("age_category", "AgeCategory", "https://schema.hbp.eu/uniminds/ageCategory", required=False, multiple=False),
      Field("cellular_target", "CellularTarget", "https://schema.hbp.eu/uniminds/cellularTarget", required=False, multiple=False),
      Field("brain_structure", "BrainStructure", "https://schema.hbp.eu/uniminds/brainStructure", required=False, multiple=False),
      Field("disability", "Disability", "https://schema.hbp.eu/uniminds/disability", required=False, multiple=False),
      Field("genotype", "Genotype", "https://schema.hbp.eu/uniminds/genotype", required=False, multiple=False),
      Field("handedness", "Handedness", "https://schema.hbp.eu/uniminds/handedness", required=False, multiple=False),
      Field("method", "Method", "https://schema.hbp.eu/uniminds/method", required=False, multiple=False),
      Field("publication", "Publication", "https://schema.hbp.eu/uniminds/publication", required=False, multiple=False),
      Field("sex", "Sex", "https://schema.hbp.eu/uniminds/sex", required=False, multiple=False),
      Field("species", "Species", "https://schema.hbp.eu/uniminds/species", required=False, multiple=False),
      Field("strain", "Strain", "https://schema.hbp.eu/uniminds/strain", required=False, multiple=False),
      Field("study_target", "StudyTarget", "https://schema.hbp.eu/uniminds/studyTarget", required=False, multiple=False),
      Field("subjectgroup", "SubjectGroup", "https://schema.hbp.eu/uniminds/subjectGroup", required=False, multiple=False),
      Field("subjects", "Subject", "https://schema.hbp.eu/uniminds/subjects", required=False, multiple=True))
    


class TissueSample(MINDSObject):
    """
    docstring
    """
    _path = "/core/tissuesample/v1.0.0"
    type = ["uniminds:TissueSample"]
    fields = (
      Field("alternatives", KGObject, "https://schema.hbp.eu/inference/alternatives", required=False, multiple=True),
      Field("identifier", basestring, "http://schema.org/identifier", required=True, multiple=False),
      Field("name", basestring, "http://schema.org/name", required=True, multiple=False),
      Field("subject", "Subject", "https://schema.hbp.eu/uniminds/subject", required=False, multiple=False))
###############################################################    
### end of script-generated code
################################################################    

def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
            if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__ == __name__]
    

class UniMINDSOption():
    pass


if __name__=='__main__':

    import os
    from fairgraph import uniminds, KGClient
    token = os.environ['HBP_token']
    client = KGClient(token)
    for cls in uniminds.list_kg_classes():
        print(cls.__name__)
        # for f in cls.fields:
        #     print('    - %s' % f.name)
