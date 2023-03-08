"""

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
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
        Field("components", ["openminds.core.Setup", "openminds.core.SoftwareVersion", "openminds.ephys.Electrode", "openminds.ephys.ElectrodeArray", "openminds.ephys.Pipette", "openminds.specimenprep.SlicingDevice"], "vocab:components", multiple=True, required=True,
              doc="no description available"),
        Field("description", str, "vocab:description", multiple=False, required=True,
              doc="Longer statement or account giving the characteristics of the setup."),
        Field("location", str, "vocab:location", multiple=False, required=False,
              doc="no description available"),
        Field("manufacturers", ["openminds.core.Consortium", "openminds.core.Organization", "openminds.core.Person"], "vocab:manufacturer", multiple=True, required=False,
              doc="no description available"),
        Field("types", "openminds.controlledterms.SetupType", "vocab:type", multiple=True, required=False,
              doc="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to."),

    ]
    existence_query_fields = ('name', 'components', 'description')
