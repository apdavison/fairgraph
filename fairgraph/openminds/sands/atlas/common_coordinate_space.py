"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class CommonCoordinateSpace(KGObject):
    """

    """
    default_space = "atlas"
    type = ["https://openminds.ebrains.eu/sands/CommonCoordinateSpace"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:fullName", multiple=False, required=True,
              doc="Whole, non-abbreviated name of the common coordinate space."),
        Field("alias", str, "vocab:shortName", multiple=False, required=True,
              doc="Shortened or fully abbreviated name of the common coordinate space."),
        Field("anatomical_axes_orientation", "openminds.controlledterms.AnatomicalAxesOrientation", "vocab:anatomicalAxesOrientation", multiple=False, required=True,
              doc="Relation between reference planes used in anatomy and mathematics."),
        Field("axes_origins", "openminds.core.QuantitativeValue", "vocab:axesOrigin", multiple=True, required=True,
              doc="Special point in a coordinate system used as a fixed point of reference for the geometry of the surrounding space."),
        Field("default_images", "openminds.core.File", "vocab:defaultImage", multiple=True, required=False,
              doc="Two or three dimensional image that particluarly represents a specific coordinate space."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the common coordinate space."),
        Field("digital_identifier", ["openminds.core.DOI", "openminds.core.ISBN", "openminds.core.RRID"], "vocab:digitalIdentifier", multiple=False, required=False,
              doc="Digital handle to identify objects or legal persons."),
        Field("homepage", "openminds.core.URL", "vocab:homepage", multiple=False, required=False,
              doc="Main website of the common coordinate space."),
        Field("how_to_cite", str, "vocab:howToCite", multiple=False, required=False,
              doc="Preferred format for citing a particular object or legal person."),
        Field("native_unit", "openminds.controlledterms.UnitOfMeasurement", "vocab:nativeUnit", multiple=False, required=True,
              doc="Determinate quantity used in the original measurement."),
        Field("ontology_identifiers", str, "vocab:ontologyIdentifier", multiple=True, required=False,
              doc="Term or code used to identify the common coordinate space registered within a particular ontology."),
        Field("release_date", date, "vocab:releaseDate", multiple=False, required=True,
              doc="Fixed date on which a product is due to become or was made available for the general public to see or buy"),
        Field("version_identifier", str, "vocab:versionIdentifier", multiple=False, required=True,
              doc="Term or code used to identify the version of something."),

    ]
    existence_query_fields = ('alias', 'version_identifier')
