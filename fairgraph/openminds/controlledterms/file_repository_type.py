"""

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - Amazon S3 repository
         - An S3 repository uses the cloud storage of the Amazon S3 service.
       * - Seafile repository
         - Seafile is an open source file sync&share solution designed for high reliability, performance and productivity.
       * - GPFS repository
         - GPFS, short for General Parallel File System is a high-performance clustered file system developed by IBM
       * - GitHub repository
         - A GitHub repository offers version control and source code management functionalities of Git, plus some GitHub features (e.g., access control, bug tracking, feature requests, task management, continous integration, and wikis).
       * - GitLab repository
         - A GitLab repository offers version control and source code management functionalities of Git, plus some GitLab features (e.g., access control, bug tracking, feature requests, task management, continous integration, and wikis).
       * - Swift repository
         - A Swift repository uses the long-term cloud storage of the OpenStack Object Store project which is particularly designed for retrieving and updating large amounts of static data without the need of a central point of control.
       * - FTP repository
         - A 'FTP repository' is located on a server that uses the file transfer protocol (FTP), a standard internet communication protocol which allows the transfer of files between clients and a server.
       * - Git repository
         - A Git repository offers version control and source code management functionalities.
       * - git-annex repository
         - git-annex allows managing large files with git, without storing the file contents in git.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class FileRepositoryType(KGObject):
    """

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - Amazon S3 repository
         - An S3 repository uses the cloud storage of the Amazon S3 service.
       * - Seafile repository
         - Seafile is an open source file sync&share solution designed for high reliability, performance and productivity.
       * - GPFS repository
         - GPFS, short for General Parallel File System is a high-performance clustered file system developed by IBM
       * - GitHub repository
         - A GitHub repository offers version control and source code management functionalities of Git, plus some GitHub features (e.g., access control, bug tracking, feature requests, task management, continous integration, and wikis).
       * - GitLab repository
         - A GitLab repository offers version control and source code management functionalities of Git, plus some GitLab features (e.g., access control, bug tracking, feature requests, task management, continous integration, and wikis).
       * - Swift repository
         - A Swift repository uses the long-term cloud storage of the OpenStack Object Store project which is particularly designed for retrieving and updating large amounts of static data without the need of a central point of control.
       * - FTP repository
         - A 'FTP repository' is located on a server that uses the file transfer protocol (FTP), a standard internet communication protocol which allows the transfer of files between clients and a server.
       * - Git repository
         - A Git repository offers version control and source code management functionalities.
       * - git-annex repository
         - git-annex allows managing large files with git, without storing the file contents in git.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/FileRepositoryType"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/",
    }
    fields = [
        Field(
            "name",
            str,
            "vocab:name",
            required=True,
            doc="Word or phrase that constitutes the distinctive designation of the file repository type.",
        ),
        Field(
            "definition",
            str,
            "vocab:definition",
            doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
        ),
        Field(
            "description",
            str,
            "vocab:description",
            doc="Longer statement or account giving the characteristics of the file repository type.",
        ),
        Field(
            "interlex_identifier",
            IRI,
            "vocab:interlexIdentifier",
            doc="Persistent identifier for a term registered in the InterLex project.",
        ),
        Field(
            "knowledge_space_link",
            IRI,
            "vocab:knowledgeSpaceLink",
            doc="Persistent link to an encyclopedia entry in the Knowledge Space project.",
        ),
        Field(
            "preferred_ontology_identifier",
            IRI,
            "vocab:preferredOntologyIdentifier",
            doc="Persistent identifier of a preferred ontological term.",
        ),
        Field(
            "synonyms",
            str,
            "vocab:synonym",
            multiple=True,
            doc="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.",
        ),
        Field(
            "describes",
            [
                "openminds.computation.ValidationTestVersion",
                "openminds.computation.WorkflowRecipeVersion",
                "openminds.core.DatasetVersion",
                "openminds.core.MetaDataModelVersion",
                "openminds.core.ModelVersion",
                "openminds.core.SoftwareVersion",
                "openminds.core.WebServiceVersion",
                "openminds.publications.Book",
                "openminds.publications.Chapter",
                "openminds.publications.LearningResource",
                "openminds.publications.LivePaperVersion",
                "openminds.publications.ScholarlyArticle",
                "openminds.sands.BrainAtlasVersion",
                "openminds.sands.CommonCoordinateSpaceVersion",
            ],
            "^vocab:keyword",
            reverse="keywords",
            multiple=True,
            doc="reverse of 'keyword'",
        ),
        Field(
            "is_type_of",
            "openminds.core.FileRepository",
            "^vocab:type",
            reverse="types",
            multiple=True,
            doc="reverse of 'type'",
        ),
    ]
    existence_query_fields = ("name",)

    def __init__(
        self,
        name=None,
        definition=None,
        description=None,
        interlex_identifier=None,
        knowledge_space_link=None,
        preferred_ontology_identifier=None,
        synonyms=None,
        describes=None,
        is_type_of=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return super().__init__(
            id=id,
            space=space,
            scope=scope,
            data=data,
            name=name,
            definition=definition,
            description=description,
            interlex_identifier=interlex_identifier,
            knowledge_space_link=knowledge_space_link,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
            describes=describes,
            is_type_of=is_type_of,
        )
