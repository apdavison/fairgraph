"""

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - EBRAINS Model Catalog
         - The EBRAINS Model Catalog contains information about models developed and/or used within the EBRAINS research infrastructure.
       * - EBRAINS Collaboratory Wiki
         - The Collaboratory Wiki is the main interface to access all other Collaboratory service provided by the EBRAINS research infrastructure.
       * - Neuroglancer
         - 'Neuroglancer' is a WebGL-based viewer for volumetric data.
       * - Zenodo
         - Zenodo is a general-purpose open repository developed under the European OpenAIRE program and operated by CERN.
       * - Multi-Image-OSd
         - Web application for viewing of series of high-resolution 2D images.
       * - siibra-explorer
         - 'siibra-explorer' is an interactive viewer for multilevel brain atlases
       * - Allen Institute Cell Types Data Portal
         - Web application for visualizing and browsing the Allen Cell Types Database.
       * - LocaliZoom
         - Web application for viewing of series of high-resolution 2D images that have been anchored to reference atlases.
       * - NeuroMorpho.Org
         - A web-based inventory dedicated to densely archive and organize all publicly shared digital reconstructions of neuronal morphology.
       * - ModelDB
         - ModelDB is a curated database of published models in the broad domain of computational neuroscience.
       * - EBRAINS Knowledge Graph Search UI
         - The EBRAINS Knowledge Graph Search User Interface is a web application for searching the EBRAINS Knowledge Graph.
       * - EBRAINS Collaboratory Lab
         - The Collaboratory Lab is a web-based JupyterLab service provided by the EBRAINS research infrastructure.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class Service(KGObject):
    """

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - EBRAINS Model Catalog
         - The EBRAINS Model Catalog contains information about models developed and/or used within the EBRAINS research infrastructure.
       * - EBRAINS Collaboratory Wiki
         - The Collaboratory Wiki is the main interface to access all other Collaboratory service provided by the EBRAINS research infrastructure.
       * - Neuroglancer
         - 'Neuroglancer' is a WebGL-based viewer for volumetric data.
       * - Zenodo
         - Zenodo is a general-purpose open repository developed under the European OpenAIRE program and operated by CERN.
       * - Multi-Image-OSd
         - Web application for viewing of series of high-resolution 2D images.
       * - siibra-explorer
         - 'siibra-explorer' is an interactive viewer for multilevel brain atlases
       * - Allen Institute Cell Types Data Portal
         - Web application for visualizing and browsing the Allen Cell Types Database.
       * - LocaliZoom
         - Web application for viewing of series of high-resolution 2D images that have been anchored to reference atlases.
       * - NeuroMorpho.Org
         - A web-based inventory dedicated to densely archive and organize all publicly shared digital reconstructions of neuronal morphology.
       * - ModelDB
         - ModelDB is a curated database of published models in the broad domain of computational neuroscience.
       * - EBRAINS Knowledge Graph Search UI
         - The EBRAINS Knowledge Graph Search User Interface is a web application for searching the EBRAINS Knowledge Graph.
       * - EBRAINS Collaboratory Lab
         - The Collaboratory Lab is a web-based JupyterLab service provided by the EBRAINS research infrastructure.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/Service"]
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
            doc="Word or phrase that constitutes the distinctive designation of the service.",
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
            doc="Longer statement or account giving the characteristics of the service.",
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
            "linked_from",
            "openminds.core.ServiceLink",
            "^vocab:service",
            reverse="services",
            multiple=True,
            doc="reverse of 'service'",
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
        linked_from=None,
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
            linked_from=linked_from,
        )
