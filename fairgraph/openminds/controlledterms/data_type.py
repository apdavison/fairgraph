"""


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - statistical data
         - https://www.wikidata.org/wiki/Q7604387
       * - scalar
         - A 'scalar' represent a single value (e.g., integer, float, string, etc.).
       * - graph data
         - 'Graph data' are composed of a finite set of edges, meaning unordered or ordered pairs of vertices (also called nodes or points) for an undirected or directed graphs, respectively.
       * - 4D vector data
         - '4D vector data' are a list of 4-dimensional vertices (4D scalar data) that defined the shape and one additional property of a spatial object.
       * - list
         - A 'list' is a series of ordered scalars and/or lists.
       * - raster graphic
         - A 'raster graphic' is a matrix, representing values (scalars, lists, matrices) on a grid in a two dimensional space, viewable via a monitor, paper, or other display medium.
       * - matrix data
         - 'Matrix data' are numbers, symbols, or expressions, arranged in rows and columns (rectangular array or table).
       * - metadata
         - 'Metadata' are data about data.
       * - 3D scalar data
         - '3D scalar data' represent a discrete geometric location (x, y, z).
       * - voxel data
         - 'Voxel data' is a matrix defining values (scalars, lists, or matrices) on a grid in a three dimensional space, which can be rendered to raster graphic.
       * - event sequence
         - An 'event sequence' is a list or matrix, where elements are ordered in not equally spaced points in time.
       * - table
         - A 'table' is an arrangement of elements (scalars, lists and/or matrices) in specified/named rows and columns.
       * - 3D vector data
         - '3D vector data' are composed of a list of vertices (3D scalar data) that defined the shape of a spatial object.
       * - spatial metadata
         - 'Spatial metadata' provide information about the identification, the extent, the quality, the spatial and temporal aspects, the content, the spatial reference, the portrayal, distribution, and other properties of spatial data.
       * - 3D computer graphic
         - A '3D computer graphic' is an associative array, defining points, lines, and/or curves in a three dimensional space, which can be rendered to raster graphic.
       * - time series
         - A 'time series' is a list or matrix, where elements are ordered in equally spaced points in time.
       * - vector graphic
         - A 'vector graphic' is an associative array defining points, lines and curves which can be rendered to a raster graphic.
       * - 4D scalar data
         - '4D scalar data' represent a discrete geometric location with one additional parameter (x, y, z, w).
       * - spatial data
         - 'Spatial data' are data with geographical properties (e.g. physical location and shape of geometric objects) that enable spatial queries.
       * - tensor data
         - 'Tensor data' describe a multilinear relationship between sets of algebraic objects (vectors, scalars, other tensors) related to a vector space.

Here we show the first 20 values, an additional 3 values are not shown.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class DataType(KGObject):
    """


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - statistical data
         - https://www.wikidata.org/wiki/Q7604387
       * - scalar
         - A 'scalar' represent a single value (e.g., integer, float, string, etc.).
       * - graph data
         - 'Graph data' are composed of a finite set of edges, meaning unordered or ordered pairs of vertices (also called nodes or points) for an undirected or directed graphs, respectively.
       * - 4D vector data
         - '4D vector data' are a list of 4-dimensional vertices (4D scalar data) that defined the shape and one additional property of a spatial object.
       * - list
         - A 'list' is a series of ordered scalars and/or lists.
       * - raster graphic
         - A 'raster graphic' is a matrix, representing values (scalars, lists, matrices) on a grid in a two dimensional space, viewable via a monitor, paper, or other display medium.
       * - matrix data
         - 'Matrix data' are numbers, symbols, or expressions, arranged in rows and columns (rectangular array or table).
       * - metadata
         - 'Metadata' are data about data.
       * - 3D scalar data
         - '3D scalar data' represent a discrete geometric location (x, y, z).
       * - voxel data
         - 'Voxel data' is a matrix defining values (scalars, lists, or matrices) on a grid in a three dimensional space, which can be rendered to raster graphic.
       * - event sequence
         - An 'event sequence' is a list or matrix, where elements are ordered in not equally spaced points in time.
       * - table
         - A 'table' is an arrangement of elements (scalars, lists and/or matrices) in specified/named rows and columns.
       * - 3D vector data
         - '3D vector data' are composed of a list of vertices (3D scalar data) that defined the shape of a spatial object.
       * - spatial metadata
         - 'Spatial metadata' provide information about the identification, the extent, the quality, the spatial and temporal aspects, the content, the spatial reference, the portrayal, distribution, and other properties of spatial data.
       * - 3D computer graphic
         - A '3D computer graphic' is an associative array, defining points, lines, and/or curves in a three dimensional space, which can be rendered to raster graphic.
       * - time series
         - A 'time series' is a list or matrix, where elements are ordered in equally spaced points in time.
       * - vector graphic
         - A 'vector graphic' is an associative array defining points, lines and curves which can be rendered to a raster graphic.
       * - 4D scalar data
         - '4D scalar data' represent a discrete geometric location with one additional parameter (x, y, z, w).
       * - spatial data
         - 'Spatial data' are data with geographical properties (e.g. physical location and shape of geometric objects) that enable spatial queries.
       * - tensor data
         - 'Tensor data' describe a multilinear relationship between sets of algebraic objects (vectors, scalars, other tensors) related to a vector space.

Here we show the first 20 values, an additional 3 values are not shown.

    """
    default_space = "controlled"
    type = ["https://openminds.ebrains.eu/controlledTerms/DataType"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the data type."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the data type."),
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
