"""
Generates fairgraph classes.

The contents of target/fairgraph should be copied into the fairgraph/openminds directory
"""

import glob
import json
import os
import sys
import re
from typing import List
from collections import defaultdict
import warnings
from jinja2 import FileSystemLoader


from generator.commons import (
    JinjaGenerator,
    TEMPLATE_PROPERTY_TYPE,
    TEMPLATE_PROPERTY_LINKED_TYPES,
    SchemaStructure,
    TEMPLATE_PROPERTY_EMBEDDED_TYPES,
    SCHEMA_FILE_ENDING,
    ROOT_PATH,
    EXPANDED_DIR,
    find_resource_directories,
)

LIST_CLASSES_TEMPATE = '''

def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
           if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__.startswith(__name__)]
'''

# for backwards compatibility or to increase clarity we remap certain
# names from the schemas when creating Python attribute names
name_map = {
    "shortName": "alias",
    "fullName": "name",
    "scope": "model_scope",
    "hasVersion": "versions",
    "hasEntity": "entities",
}

# in general we make attribute names plural when the attribute can contain multiple items
# the following dict contains exceptions to the simple rule we use for making names plural
# (i.e. add 's' unless the word already ends in 's')
custom_multiple = {
    "data": "data",
    "input_data": "input_data",
    "output_data": "output_data",
    "reference_data": "reference_data",
    "funding": "funding",
    "biological_sex": "biological_sex",
    "age_category": "age_categories",
    "descended_from": "descended_from",
    "laterality": "laterality",
    "software": "software",
    "configuration": "configuration",
    "is_part_of": "is_part_of",
    "semantically_anchored_to": "semantically_anchored_to",
    "is_alternative_version_of": "is_alternative_version_of",
    "experimental_approach": "experimental_approaches",
    "pathology": "pathologies",
    "uncertainty": "uncertainties",
    "application_category": "application_categories",
    "about": "about",
    "performed_by": "performed_by",
    "grouped_by": "grouped_by",
    "hash": "hash",
}

# in a small number of cases, a single item is allowed but this item itself has an
# array-like character, e.g. PropertyValueList
custom_singular = {"environment_variable": "environment_variables"}


def generate_python_name(json_name, allow_multiple=False):
    if json_name in name_map:
        python_name = name_map[json_name]
    else:
        python_name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", json_name)
        python_name = re.sub("([a-z0-9])([A-Z])", r"\1_\2", python_name).lower()
        if allow_multiple and python_name[-1] != "s":
            if python_name in custom_multiple:
                python_name = custom_multiple[python_name]
            else:
                python_name += "s"
        elif python_name in custom_singular:
            python_name = custom_singular[python_name]
    return python_name


type_name_map = {"string": "str", "integer": "int", "number": "float", "array": "list"}

format_map = {
    "iri": "IRI",
    "date": "date",
    "date-time": "datetime",
    "time": "datetime",
    "email": "str",  # could maybe use Pydantic or something to be stricter about this
    "ECMA262": "str",
}


def generate_class_name(iri):
    parts = iri.split("/")[-2:]
    for i in range(len(parts) - 1):
        parts[i] = parts[i].lower()
    return "openminds." + ".".join(parts)


def generate_doc(property, obj_title):
    if obj_title.upper() == obj_title:  # for acronyms, e.g. DOI
        obj_title_readable = obj_title
    elif "UBERON" in obj_title:
        obj_title_readable = obj_title
    else:
        obj_title_readable = re.sub("([A-Z])", " \g<0>", obj_title).strip().lower()
    doc = property.get("description", "no description available")
    doc = doc.replace("someone or something", f"the {obj_title_readable}")
    doc = doc.replace("something or somebody", f"the {obj_title_readable}")
    doc = doc.replace("something or someone", f"the {obj_title_readable}")
    doc = doc.replace("a being or thing", f"the {obj_title_readable}")
    return doc


def invert_dict(D):
    newD = {}
    for key, values in D.items():
        for value in values:
            newD[value] = key
    return newD


DEFAULT_SPACES = {
    "chemicals": {"default": "dataset"},
    "core": invert_dict(
        {
            "common": [
                "Affiliation",
                "Comment",
                "Configuration",
                "Consortium",
                "Funding",
                "GRIDID",
                "HANDLE",
                "HardwareSystem",
                "IdentifiersDotOrgID",
                "ORCID",
                "Organization",
                "Person",
                "Project",
                "Query",
                "RORID",
                "TermSuggestion",
                "WebResource",
                "RRID",
                "AccountInformation",  # or does this go in "restricted"?
            ],
            "files": [
                "ContentTypePattern",
                "File",
                "FileBundle",
                "FilePathPattern",
                "FileRepositoryStructure",
                "Hash",
            ],
            "dataset": [
                "Contribution",
                "Copyright",
                "DOI",
                "Dataset",
                "DatasetVersion",
                "FileArchive",
                "FileRepository",
                "ISBN",
                "ISSN",
                "NumericalParameter",
                "ParameterSet",
                "PropertyValueList",
                "Protocol",
                "ExperimentalActivity",
                "ProtocolExecution",
                "QuantitativeValue",
                "QuantitativeValueRange",
                "QuantitativeValueArray",
                "ResearchProductGroup",
                "ServiceLink",
                "StringParameter",
                "Subject",
                "SubjectGroup",
                "SubjectGroupState",
                "SubjectState",
                "TissueSample",
                "TissueSampleCollection",
                "TissueSampleCollectionState",
                "TissueSampleState",
                "BehavioralProtocol",
                "Stimulation",
                "Strain",
                "Setup",
            ],
            "model": ["Model", "ModelVersion"],
            "software": ["SWHID", "Software", "SoftwareVersion"],
            "restricted": ["ContactInformation"],
            "metadatamodel": ["MetaDataModel", "MetaDataModelVersion"],
            "controlled": ["License", "ContentType"],
            "webservice": ["WebService", "WebServiceVersion"],
        }
    ),
    "computation": {"default": "computation"},
    "controlledTerms": {"default": "controlled"},
    "SANDS": invert_dict(
        {
            "spatial": [
                "AnatomicalEntity",
                "Annotation",
                "CoordinatePoint",
                "CustomAnatomicalEntity",
                "CustomAnnotation",
                "CustomCoordinateSpace",
                "Image",
                "QualitativeRelationAssessment",
                "QuantitativeRelationAssessment",
            ],
            "atlas": [
                "AnatomicalTargetPosition",
                "AtlasAnnotation",
                "BrainAtlas",
                "BrainAtlasVersion",
                "Circle",
                "ColorMap",
                "CommonCoordinateSpace",
                "CommonCoordinateSpaceVersion",
                "CoordinatePoint",
                "Ellipse",
                "ParcellationEntity",
                "ParcellationTerminology",
                "ParcellationTerminologyVersion",
                "ParcellationEntityVersion",
                "Rectangle",
                "SingleColor",
            ],
        }
    ),
    "publications": {"default": "livepapers"},
    "ephys": {"default": "in-depth"},
    "chemicals": {"default": "in-depth"},
    "specimenPrep": {"default": "in-depth"},
    "stimulation": {"default": "in-depth"},
}


def get_default_space(schema_group, cls_name):
    if schema_group not in DEFAULT_SPACES:
        raise Exception(f"Please update DEFAULT_SPACES for the {schema_group} module")
    if cls_name in DEFAULT_SPACES[schema_group]:
        return DEFAULT_SPACES[schema_group][cls_name]
    else:
        try:
            return DEFAULT_SPACES[schema_group]["default"]
        except KeyError:
            raise KeyError(f"An entry for '{cls_name}' is missing from DEFAULT_SPACES['{schema_group}']")


# in general, we use the required fields when deciding whether a given object already exists
# in the KG. Sometimes this method is inappropriate or undesired, and so for some classes
# we use a custom set of fields.
custom_existence_queries = {
    "LaunchConfiguration": ("executable", "name"),
    "Person": ("given_name", "family_name"),
    "File": ("iri", "hash"),
    "FileRepository": ("iri",),
    "License": ("alias",),
    "DOI": ("identifier",),
    "GRIDID": ("identifier",),
    "HANDLE": ("identifier",),
    "ISBN": ("identifier",),
    "ORCID": ("identifier",),
    "RORID": ("identifier",),
    "SWHID": ("identifier",),
    "WebResource": ("iri",),
    "Dataset": ("alias",),
    "DatasetVersion": ("alias", "version_identifier"),
    "MetaDataModel": ("alias",),
    "MetaDataModelVersion": ("alias", "version_identifier"),
    "Model": ("name",),  # here we use 'name' instead of 'alias' for backwards compatibility
    "ModelVersion": ("name", "version_identifier"),
    "Project": ("alias",),
    "Software": ("alias",),
    "SoftwareVersion": ("alias", "version_identifier"),
    "Protocol": ("name",),
    "BrainAtlas": ("digital_identifier",),
    "BrainAtlasVersion": ("alias", "version_identifier"),
    "CommonCoordinateSpace": ("alias", "version_identifier"),
    "ParcellationEntity": ("name",),
    "ParcellationEntityVersion": ("name", "version_identifier"),
    "ParcellationTerminologyVersion": ("alias", "version_identifier"),
    "CustomCoordinateSpace": ("name",),
    "WorkflowRecipe": ("name",),
    "WorkflowRecipeVersion": ("name", "version_identifier"),
    "ValidationTest": ("name", "alias"),
    "ValidationTestVersion": ("alias", "version_identifier"),
    "LivePaper": ("name", "alias"),
    "LivePaperVersion": ("alias", "version_identifier"),
    "LivePaperResourceItem": ("name", "iri", "is_part_of"),
    "ScholarlyArticle": ("name",),
    "WorkflowExecution": ("stages",),
    "Configuration": ("configuration",),
    "Periodical": ("abbreviation",),
}


def get_existence_query(cls_name, fields):
    if cls_name in custom_existence_queries:
        return custom_existence_queries[cls_name]

    for field in fields:
        if field["name"] == "lookup_label":
            return ("lookup_label",)

    required_field_names = []
    for field in fields:
        if field["required"]:
            required_field_names.append(field["name"])
    return tuple(required_field_names)


def property_name_sort_key(arg):
    """Sort the name field to be first"""
    name, property = arg
    priorities = {
        "name": "0",
        "fullName": "1",
        "shortName": "2",
        "lookupLabel": "3",
    }
    return priorities.get(name, name)


def get_controlled_terms_table(type_):
    from kg_core.kg import kg
    from kg_core.request import Stage, Pagination

    host = "core.kg.ebrains.eu"
    limit = 20
    try:
        token = os.environ["KG_AUTH_TOKEN"]
    except KeyError:
        warnings.warn(
            "Cannot get controlled terms."
            "Please obtain an EBRAINS auth token and put it in an environment variable 'KG_AUTH_TOKEN'"
        )
        return ""
    kg_client = kg(host).with_token(token).build()
    response = kg_client.instances.list(
        stage=Stage.RELEASED,
        target_type=type_,
        space="controlled",
        pagination=Pagination(start=0, size=limit),
    )
    if response.error:
        warnings.warn(f"Error trying to retrieve values for {type_}: {response.error}")
        return ""
    else:
        if response.total == 0:
            return ""
        lines = []
        if response.total > response.size:
            assert response.size == limit
            lines.extend(
                [
                    "",
                    f"    Here we show the first {limit} possible values, an additional {response.total - limit} values are not shown.",
                ]
            )
        lines.extend(
            [
                "",
                "    .. list-table:: **Possible values**",
                "       :widths: 20 80",
                "       :header-rows: 0",
                "",
            ]
        )
        for item in response.data:
            vocab = "https://openminds.ebrains.eu/vocab"
            name = item[f"{vocab}/name"]
            definition = item.get(f"{vocab}/definition", None)
            link = item.get(f"{vocab}/preferredOntologyIdentifier", None)
            if definition is None:
                definition = link or " "
            if link:
                name = f"`{name} <{link}>`_"
            lines.append(f"       * - {name}")
            lines.append(f"         - {definition}")
        lines.append("")
        return "\n".join(lines)


class FairgraphGenerator(JinjaGenerator):
    def __init__(self, schema_information: List[SchemaStructure]):
        super().__init__("py", None, "fairgraph_module_template.py.txt")
        self.env.loader = FileSystemLoader(os.path.dirname(os.path.realpath(__file__)))
        self.target_path = os.path.join("..", "fairgraph", "openminds")
        self.schema_information = schema_information
        self.schema_information_by_type = {}
        # self.schema_collection_by_group = {}
        for s in self.schema_information:
            self.schema_information_by_type[s.type] = s
        self.import_data = defaultdict(dict)

    def _pre_process_template(self, schema):
        schema_information = self.schema_information_by_type[schema[TEMPLATE_PROPERTY_TYPE]]
        schema["simpleTypeName"] = os.path.basename(schema[TEMPLATE_PROPERTY_TYPE])
        schema["schemaGroup"] = schema_information.schema_group.split("/")[0]
        schema["schemaVersion"] = schema_information.version
        # if schema["schemaGroup"] not in self.schema_collection_by_group:
        #     self.schema_collection_by_group[schema["schemaGroup"]] = []
        # self.schema_collection_by_group[schema["schemaGroup"]].append(schema_information)

        fields = []
        # imports = set([])
        for name, property in sorted(schema["properties"].items(), key=property_name_sort_key):
            allow_multiple = False
            if property.get("type") == "array":
                allow_multiple = True
            if TEMPLATE_PROPERTY_LINKED_TYPES in property:
                possible_types = [f'"{generate_class_name(iri)}"' for iri in property[TEMPLATE_PROPERTY_LINKED_TYPES]]
            elif TEMPLATE_PROPERTY_EMBEDDED_TYPES in property:
                possible_types = [
                    f'"{generate_class_name(iri)}"' for iri in property[TEMPLATE_PROPERTY_EMBEDDED_TYPES]
                ]  # todo: handle minItems maxItems, e.g. for axesOrigin
            elif "_formats" in property:
                assert property["type"] == "string"
                possible_types = sorted(set([format_map[item] for item in property["_formats"]]))
            elif property.get("type") == "array":
                possible_types = [type_name_map[property["items"]["type"]]]
            else:
                possible_types = [type_name_map[property["type"]]]
            # imports.update(possible_types)
            if len(possible_types) == 1:
                possible_types_str = possible_types[0]
            else:
                possible_types_str = "[{}]".format(", ".join(sorted(possible_types)))
            field = {
                "name": generate_python_name(name, allow_multiple),
                "type": possible_types_str,
                "iri": f"vocab:{name}",
                "allow_multiple": allow_multiple,
                "required": name in schema.get("required", []),
                "doc": generate_doc(property, schema["simpleTypeName"]),
            }
            fields.append(field)

        # for builtin_type in ("str", "int", "float"):
        #     try:
        #         imports.remove(builtin_type)
        #     except KeyError:
        #         pass

        # if imports:
        #     if len(imports) == 1:
        #         import_str = f"from fairgraph.openminds.?? import {list(imports)[0]}"
        #     else:
        #         import_str = "from fairgraph.openminds.?? import ({})".format(", ".join(sorted(imports)))
        # else:
        #     import_str = ""

        # if a given type is found both linked and embedded we use KGObject
        if schema["_type"] in self._embedded_types and not schema["_type"] in self._linked_types:
            base_class = "EmbeddedMetadata"
            default_space = None
        else:
            base_class = "KGObject"
            default_space = get_default_space(schema["schemaGroup"], schema["simpleTypeName"])
        context = {
            # "imports": import_str,
            "class_name": generate_class_name(schema[TEMPLATE_PROPERTY_TYPE]).split(".")[-1],
            "default_space": default_space,
            "base_class": base_class,
            "openminds_type": schema[TEMPLATE_PROPERTY_TYPE],
            "docstring": schema.get("description", ""),
            "fields": fields,
            "existence_query_fields": get_existence_query(schema["simpleTypeName"], fields),
            "preamble": preamble.get(schema["simpleTypeName"], ""),
            "additional_methods": additional_methods.get(schema["simpleTypeName"], ""),
        }
        if base_class == "KGObject":
            context["standard_init_fields"] = "id=id, space=space, scope=scope, "
        else:
            context["standard_init_fields"] = ""
        if schema["schemaGroup"] == "controlledTerms":
            context["docstring"] += get_controlled_terms_table(schema["_type"])
        schema.update(context)
        self.import_data[schema["schemaGroup"]][schema[TEMPLATE_PROPERTY_TYPE]] = {"class_name": context["class_name"]}
        return schema

    def _process_template(self, schema) -> str:
        result = super()._process_template(schema)
        return strip_trailing_whitespace(result)

    def _generate_target_file_path(self, schema_group, schema_group_path, schema_path):
        relative_schema_path = os.path.dirname(schema_path[len(schema_group_path) + 1 :])
        relative_schema_path = relative_schema_path.replace("-", "_")
        schema_file_name = os.path.basename(schema_path)
        schema_file_name_without_extension = generate_python_name(schema_file_name[: -len(SCHEMA_FILE_ENDING)])
        schema_group = schema_group.split("/")[0].lower()
        target_path = os.path.join(
            self.target_path,
            schema_group,
            relative_schema_path,
            f"{schema_file_name_without_extension}.{self.format}",
        )
        return target_path

    def _generate_additional_files(self, schema_group, schema_group_path, schema_path, schema):
        relative_schema_path = os.path.dirname(schema_path[len(schema_group_path) + 1 :])
        relative_schema_path = relative_schema_path.replace("-", "_")
        schema_group = schema_group.split("/")[0]
        path_parts = (self.target_path, schema_group.lower(), *relative_schema_path.split("/"))
        # create directories
        os.makedirs(os.path.join(*path_parts), exist_ok=True)
        # write __init__.py files
        schema_file_name = os.path.basename(schema_path)
        path = (
            relative_schema_path.replace("/", ".")
            + f".{generate_python_name(schema_file_name[:-len(SCHEMA_FILE_ENDING)])}"
        )
        if path[0] != ".":
            path = "." + path
        self.import_data[schema_group][schema[TEMPLATE_PROPERTY_TYPE]]["path"] = path

        for i in range(len(path_parts) + 1):
            path = os.path.join(*path_parts[:i], "__init__.py")
            if not os.path.exists(path):
                with open(path, "w") as fp:
                    fp.write("")

    def _pre_generate(self, ignore=None):
        self._linked_types = set()
        self._embedded_types = set()
        _linked_from = defaultdict(list)
        _embedded_in = defaultdict(list)
        expanded_path = os.path.join(ROOT_PATH, EXPANDED_DIR)
        for schema_group in find_resource_directories(expanded_path, file_ending=SCHEMA_FILE_ENDING, ignore=ignore):
            schema_group_path = os.path.join(expanded_path, schema_group)
            for schema_path in glob.glob(os.path.join(schema_group_path, f"**/*{SCHEMA_FILE_ENDING}"), recursive=True):
                with open(schema_path, "r") as schema_file:
                    schema = json.load(schema_file)
                for property in schema["properties"].values():
                    if TEMPLATE_PROPERTY_EMBEDDED_TYPES in property:
                        self._embedded_types.update(property[TEMPLATE_PROPERTY_EMBEDDED_TYPES])
                        for item in property[TEMPLATE_PROPERTY_EMBEDDED_TYPES]:
                            _embedded_in[item].append(schema["_type"])
                    elif TEMPLATE_PROPERTY_LINKED_TYPES in property:
                        self._linked_types.update(property[TEMPLATE_PROPERTY_LINKED_TYPES])
                        for item in property[TEMPLATE_PROPERTY_LINKED_TYPES]:
                            _linked_from[item].append(schema["_type"])
        conflicts = self._linked_types.intersection(self._embedded_types)
        if len(conflicts) > 0:
            for type_ in conflicts:
                warnings.warn(f"{type_} is linked from {_linked_from[type_]} and embedded in {_embedded_in[type_]}")

    def generate(self, ignore=None):
        super().generate(ignore=ignore)
        for schema_group, group_contents in self.import_data.items():
            path = os.path.join(self.target_path, schema_group, "__init__.py")
            with open(path, "w") as fp:
                fp.write("import sys\nimport inspect\nfrom fairgraph.kgobject import KGObject\n\n")
                for module in group_contents.values():
                    fp.write(f"from {module['path']} import {module['class_name']}\n")
                fp.write(LIST_CLASSES_TEMPATE)
        path = os.path.join(self.target_path, "__init__.py")
        with open(path, "w") as fp:
            module_names = sorted(key.lower() for key in self.import_data)
            fp.write("from . import {}\n".format(", ".join(module_names)))


def strip_trailing_whitespace(s):
    return "\n".join([line.rstrip() for line in s.splitlines()])


preamble = {
    "File": """import os
import hashlib
import mimetypes
from pathlib import Path
from urllib.request import urlretrieve
from urllib.parse import quote, urlparse, urlunparse
from .hash import Hash
from .content_type import ContentType
from ..miscellaneous.quantitative_value import QuantitativeValue
from ...controlledterms.unit_of_measurement import UnitOfMeasurement
from fairgraph.utility import accepted_terms_of_use

mimetypes.init()

def sha1sum(filename):
    BUFFER_SIZE = 128*1024
    h = hashlib.sha1()
    with open(filename, 'rb') as fp:
        while True:
            data = fp.read(BUFFER_SIZE)
            if not data:
                break
            h.update(data)
    return h.hexdigest()
    """,
    "DatasetVersion": """from urllib.request import urlretrieve
from pathlib import Path
from ....utility import accepted_terms_of_use""",
    "ModelVersion": """from fairgraph.errors import ResolutionFailure
from .model import Model""",
    "ValidationTestVersion": """from fairgraph.errors import ResolutionFailure
from .validation_test import ValidationTest""",
    "LivePaperVersion": """from fairgraph.errors import ResolutionFailure
from .live_paper import LivePaper""",
    "ScholarlyArticle": """from fairgraph.base import as_list
from .publication_issue import PublicationIssue
from .periodical import Periodical""",
    "SoftwareVersion": """from fairgraph.errors import ResolutionFailure
from .software import Software""",
    "WebServiceVersion": """from fairgraph.errors import ResolutionFailure
from .web_service import WebService""",
}

additional_methods = {
    "Person": """
    @property
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def me(cls, client, allow_multiple=False, follow_links=0):
        user_info = client.user_info()
        possible_matches = cls.list(
            client, scope="in progress", space="common",
            follow_links=follow_links,
            family_name=user_info.family_name,
            given_name=user_info.given_name
        )
        if len(possible_matches) == 0:
            person = Person(family_name=user_info.family_name,
                            given_name=user_info.given_name)
        elif len(possible_matches) == 1:
            person = possible_matches[0]
        elif allow_multiple:
            person = possible_matches
        else:
            raise Exception("Found multiple matches")
        return person
    """,
    "File": """
    @classmethod
    def from_local_file(cls, relative_path):
        cls.set_strict_mode(False)
        obj = cls(
            name=relative_path,
            storage_size=QuantitativeValue(value=float(
                os.stat(relative_path).st_size), unit=UnitOfMeasurement(name="bytes")),
            hash=Hash(algorithm="SHA1", digest=sha1sum(relative_path)),
            format=ContentType(name=mimetypes.guess_type(relative_path)[0])
            # todo: query ContentTypes since that contains additional, EBRAINS-specific content types
        )
        cls.set_strict_mode(True)
        return obj

    def download(self, local_path, client, accept_terms_of_use=False):
        if accepted_terms_of_use(client, accept_terms_of_use=accept_terms_of_use):
            local_path = Path(local_path)
            if local_path.is_dir():
                local_filename = local_path / self.name
            else:
                local_filename = local_path
                local_filename.parent.mkdir(parents=True, exist_ok=True)
            url_parts = urlparse(self.iri.value)
            url_parts = url_parts._replace(path=quote(url_parts.path))
            url = urlunparse(url_parts)
            local_filename, headers = urlretrieve(url, local_filename)
            # todo: check hash value of downloaded file
            # todo: if local_path isn't an existing directory but looks like a directory name
            #       rather than a filename, create that directory and save a file called self.name
            #       within it
            return local_filename
    """,
    "DatasetVersion": """
    def download(self, local_path, client, accept_terms_of_use=False):
        if accepted_terms_of_use(client, accept_terms_of_use=accept_terms_of_use):
            repo = self.repository.resolve(client, scope=self.scope or None)
            if (repo.iri.value.startswith("https://object.cscs.ch/v1/AUTH")
                or repo.iri.value.startswith("https://data-proxy.ebrains.eu/api/v1/public")
            ):
                zip_archive_url = f"https://data.kg.ebrains.eu/zip?container={repo.iri.value}"
            else:
                raise NotImplementedError("Download not yet implemented for this repository type")
            if local_path.endswith(".zip"):
                local_filename = Path(local_path)
            else:
                local_filename = Path(local_path) / (zip_archive_url.split("/")[-1] + ".zip")
            local_filename.parent.mkdir(parents=True, exist_ok=True)
            local_filename, headers = urlretrieve(zip_archive_url, local_filename)
            return local_filename, repo.iri.value
    """,
    "ModelVersion": """
    def is_version_of(self, client):
        parents = Model.list(client, scope=self.scope, space=self.space, versions=self)
        if len(parents) == 0:
            raise ResolutionFailure("Unable to find parent")
        else:
            assert len(parents) == 1
            return parents[0]
    """,
    "ValidationTestVersion": """
    def is_version_of(self, client):
        parents = ValidationTest.list(client, scope=self.scope, space=self.space, versions=self)
        if len(parents) == 0:
            raise ResolutionFailure("Unable to find parent")
        else:
            assert len(parents) == 1
            return parents[0]
    """,
    "LivePaperVersion": """    def is_version_of(self, client):
        parents = LivePaper.list(client, scope=self.scope, space=self.space, versions=self)
        if len(parents) == 0:
            raise ResolutionFailure("Unable to find parent")
        else:
            assert len(parents) == 1
            return parents[0]
    """,
    "ScholarlyArticle": """    def get_journal(self, client, with_volume=False, with_issue=False):
        journal = volume = issue = None
        if self.is_part_of:
            issue_or_volume = self.is_part_of.resolve(client, scope=self.scope, follow_links=1)
            if isinstance(issue_or_volume, PublicationIssue):
                volume = issue_or_volume.is_part_of
                issue = issue_or_volume
            else:
                volume = issue_or_volume
                issue = None
            journal = volume.is_part_of
            assert isinstance(journal, Periodical)
        retval = [journal]
        if with_volume:
            retval.append(volume)
        if with_issue:
            retval.append(issue)
        if not with_volume and not with_issue:
            return journal
        else:
            return tuple(retval)

    def get_citation_string(self, client):
        #Eyal, G., Verhoog, M. B., Testa-Silva, G., Deitcher, Y., Lodder, '
        #     -              'J. C., Benavides-Piccione, R., ... & Segev, I. (2016). Unique '
        #     -              'membrane properties and enhanced signal processing in human '
        #     -              'neocortical neurons. Elife, 5, e16553.
        self.resolve(client, follow_links=1)
        authors = as_list(self.authors)
        if len(authors) == 1:
            author_str = authors[0].full_name
        elif len(authors) > 1:
            author_str = ", ".join(au.full_name for au in authors[:-1])
            author_str += " & " + self.authors[-1].full_name
        journal, volume, issue = self.get_journal(client, with_volume=True, with_issue=True)
        title = self.name
        if title and title[-1] != ".":
            title += "."
        journal_name = journal.name if journal else ""
        volume_number = volume.volume_number if volume else ""
        return f"{author_str} ({self.publication_date.year}). {title} {journal_name}, {volume_number}: {self.pagination}."
    """,
    "SoftwareVersion": """    def is_version_of(self, client):
        parents = Software.list(client, scope=self.scope, space=self.space, versions=self)
        if len(parents) == 0:
            raise ResolutionFailure("Unable to find parent")
        else:
            assert len(parents) == 1
            return parents[0]
    """,
    "WebServiceVersion": """    def is_version_of(self, client):
        parents = WebService.list(client, scope=self.scope, space=self.space, versions=self)
        if len(parents) == 0:
            raise ResolutionFailure("Unable to find parent")
        else:
            assert len(parents) == 1
            return parents[0]
    """,
}

if __name__ == "__main__":
    FairgraphGenerator([]).generate()
