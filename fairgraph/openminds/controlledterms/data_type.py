"""

    Here we show the first 20 possible values, an additional 3 values are not shown.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `statistical data <https://www.wikidata.org/wiki/Q7604387>`_
         - https://www.wikidata.org/wiki/Q7604387
       * - `scalar <https://www.wikidata.org/wiki/Q1289248>`_
         - A 'scalar' represent a single value (e.g., integer, float, string, etc.).
       * - `graph data <https://www.wikidata.org/wiki/Q2479726>`_
         - 'Graph data' are composed of a finite set of edges, meaning unordered or ordered pairs of vertices (also called nodes or points) for an undirected or directed graphs, respectively.
       * - `4D vector data <https://www.wikidata.org/wiki/Q24894150>`_
         - '4D vector data' are a list of 4-dimensional vertices (4D scalar data) that defined the shape and one additional property of a spatial object.
       * - `list <https://www.wikidata.org/wiki/Q12139612>`_
         - A 'list' is a series of ordered scalars and/or lists.
       * - `raster graphic <https://www.wikidata.org/wiki/Q182270>`_
         - A 'raster graphic' is a matrix, representing values (scalars, lists, matrices) on a grid in a two dimensional space, viewable via a monitor, paper, or other display medium.
       * - `matrix data <https://www.wikidata.org/wiki/Q44337>`_
         - 'Matrix data' are numbers, symbols, or expressions, arranged in rows and columns (rectangular array or table).
       * - `metadata <https://www.wikidata.org/wiki/Q180160>`_
         - 'Metadata' are data about data.
       * - 3D scalar data
         - '3D scalar data' represent a discrete geometric location (x, y, z).
       * - voxel data
         - 'Voxel data' is a matrix defining values (scalars, lists, or matrices) on a grid in a three dimensional space, which can be rendered to raster graphic.
       * - event sequence
         - An 'event sequence' is a list or matrix, where elements are ordered in not equally spaced points in time.
       * - `table <https://www.wikidata.org/wiki/Q496946>`_
         - A 'table' is an arrangement of elements (scalars, lists and/or matrices) in specified/named rows and columns.
       * - 3D vector data
         - '3D vector data' are composed of a list of vertices (3D scalar data) that defined the shape of a spatial object.
       * - `spatial metadata <https://www.wikidata.org/wiki/Q1477538>`_
         - 'Spatial metadata' provide information about the identification, the extent, the quality, the spatial and temporal aspects, the content, the spatial reference, the portrayal, distribution, and other properties of spatial data.
       * - `3D computer graphic <https://www.wikidata.org/wiki/Q189177>`_
         - A '3D computer graphic' is an associative array, defining points, lines, and/or curves in a three dimensional space, which can be rendered to raster graphic.
       * - `time series <https://www.wikidata.org/wiki/Q186588>`_
         - A 'time series' is a list or matrix, where elements are ordered in equally spaced points in time.
       * - `vector graphic <https://www.wikidata.org/wiki/Q170130>`_
         - A 'vector graphic' is an associative array defining points, lines and curves which can be rendered to a raster graphic.
       * - 4D scalar data
         - '4D scalar data' represent a discrete geometric location with one additional parameter (x, y, z, w).
       * - `spatial data <https://www.wikidata.org/wiki/Q11692743>`_
         - 'Spatial data' are data with geographical properties (e.g. physical location and shape of geometric objects) that enable spatial queries.
       * - `tensor data <https://www.wikidata.org/wiki/Q188524>`_
         - 'Tensor data' describe a multilinear relationship between sets of algebraic objects (vectors, scalars, other tensors) related to a vector space.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class DataType(KGObject):
    """

    Here we show the first 20 possible values, an additional 3 values are not shown.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - `statistical data <https://www.wikidata.org/wiki/Q7604387>`_
         - https://www.wikidata.org/wiki/Q7604387
       * - `scalar <https://www.wikidata.org/wiki/Q1289248>`_
         - A 'scalar' represent a single value (e.g., integer, float, string, etc.).
       * - `graph data <https://www.wikidata.org/wiki/Q2479726>`_
         - 'Graph data' are composed of a finite set of edges, meaning unordered or ordered pairs of vertices (also called nodes or points) for an undirected or directed graphs, respectively.
       * - `4D vector data <https://www.wikidata.org/wiki/Q24894150>`_
         - '4D vector data' are a list of 4-dimensional vertices (4D scalar data) that defined the shape and one additional property of a spatial object.
       * - `list <https://www.wikidata.org/wiki/Q12139612>`_
         - A 'list' is a series of ordered scalars and/or lists.
       * - `raster graphic <https://www.wikidata.org/wiki/Q182270>`_
         - A 'raster graphic' is a matrix, representing values (scalars, lists, matrices) on a grid in a two dimensional space, viewable via a monitor, paper, or other display medium.
       * - `matrix data <https://www.wikidata.org/wiki/Q44337>`_
         - 'Matrix data' are numbers, symbols, or expressions, arranged in rows and columns (rectangular array or table).
       * - `metadata <https://www.wikidata.org/wiki/Q180160>`_
         - 'Metadata' are data about data.
       * - 3D scalar data
         - '3D scalar data' represent a discrete geometric location (x, y, z).
       * - voxel data
         - 'Voxel data' is a matrix defining values (scalars, lists, or matrices) on a grid in a three dimensional space, which can be rendered to raster graphic.
       * - event sequence
         - An 'event sequence' is a list or matrix, where elements are ordered in not equally spaced points in time.
       * - `table <https://www.wikidata.org/wiki/Q496946>`_
         - A 'table' is an arrangement of elements (scalars, lists and/or matrices) in specified/named rows and columns.
       * - 3D vector data
         - '3D vector data' are composed of a list of vertices (3D scalar data) that defined the shape of a spatial object.
       * - `spatial metadata <https://www.wikidata.org/wiki/Q1477538>`_
         - 'Spatial metadata' provide information about the identification, the extent, the quality, the spatial and temporal aspects, the content, the spatial reference, the portrayal, distribution, and other properties of spatial data.
       * - `3D computer graphic <https://www.wikidata.org/wiki/Q189177>`_
         - A '3D computer graphic' is an associative array, defining points, lines, and/or curves in a three dimensional space, which can be rendered to raster graphic.
       * - `time series <https://www.wikidata.org/wiki/Q186588>`_
         - A 'time series' is a list or matrix, where elements are ordered in equally spaced points in time.
       * - `vector graphic <https://www.wikidata.org/wiki/Q170130>`_
         - A 'vector graphic' is an associative array defining points, lines and curves which can be rendered to a raster graphic.
       * - 4D scalar data
         - '4D scalar data' represent a discrete geometric location with one additional parameter (x, y, z, w).
       * - `spatial data <https://www.wikidata.org/wiki/Q11692743>`_
         - 'Spatial data' are data with geographical properties (e.g. physical location and shape of geometric objects) that enable spatial queries.
       * - `tensor data <https://www.wikidata.org/wiki/Q188524>`_
         - 'Tensor data' describe a multilinear relationship between sets of algebraic objects (vectors, scalars, other tensors) related to a vector space.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/DataType"]
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
            doc="Word or phrase that constitutes the distinctive designation of the data type.",
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
            doc="Longer statement or account giving the characteristics of the data type.",
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
            "is_data_type_of",
            ["openminds.computation.LocalFile", "openminds.core.ContentType", "openminds.core.File"],
            "^vocab:dataType",
            reverse="data_types",
            multiple=True,
            doc="reverse of 'dataType'",
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
        is_data_type_of=None,
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
            is_data_type_of=is_data_type_of,
        )
