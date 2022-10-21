"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class Setup(KGObject):
    """

    """
    default_space = "dataset"
    type = ["https://openminds.ebrains.eu/core/Setup"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the setup."),
        Field("components", ["openminds.core.Setup", "openminds.core.SoftwareVersion", "openminds.ephys.Electrode", "openminds.ephys.ElectrodeArray", "openminds.ephys.Pipette"], "vocab:components", multiple=True, required=True,
              doc="no description available"),
        Field("description", str, "vocab:description", multiple=False, required=True,
              doc="Longer statement or account giving the characteristics of the setup."),
        Field("location", str, "vocab:location", multiple=False, required=False,
              doc="no description available"),
        Field("manufacturers", ["openminds.core.Organization", "openminds.core.Person"], "vocab:manufacturer", multiple=True, required=False,
              doc="no description available"),
        Field("setup_types", "openminds.controlledterms.SetupType", "vocab:setupType", multiple=True, required=False,
              doc="no description available"),

    ]
    existence_query_fields = ('name', 'components', 'description')
