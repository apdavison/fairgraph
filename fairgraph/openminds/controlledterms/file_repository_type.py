"""


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

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

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class FileRepositoryType(KGObject):
    """


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

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

    """
    default_space = "controlled"
    type = ["https://openminds.ebrains.eu/controlledTerms/FileRepositoryType"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the file repository type."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the file repository type."),
        Field("interlex_identifier", IRI, "vocab:interlexIdentifier", multiple=False, required=False,
              doc="Persistent identifier for a term registered in the InterLex project."),
        Field("knowledge_space_link", IRI, "vocab:knowledgeSpaceLink", multiple=False, required=False,
              doc="Persistent link to an encyclopedia entry in the Knowledge Space project."),
        Field("preferred_ontology_identifier", IRI, "vocab:preferredOntologyIdentifier", multiple=False, required=False,
              doc="Persistent identifier of a preferred ontological term."),
        Field("synonyms", str, "vocab:synonym", multiple=True, required=False,
              doc="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses."),

    ]
    existence_query_fields = ('name',)
