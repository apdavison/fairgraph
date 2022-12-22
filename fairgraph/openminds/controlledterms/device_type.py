"""


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - vibrating microtome
         - A 'vibrating microtome' is an mechanical instrument with a vibrating steel blade used to cut (typically) biological specimens into thin segments for further treatment and ultimately microscopic or histologic examination.
       * - CT scanner
         - A 'CT scanner' is an x-ray machine that creates and combines serial two-dimensional x-ray images (sections) with the aid of a computer to generate cross-sectional views and/or three-dimensional images of internal body structures (e.g., bones, blood vessels or soft tissues).
       * - magnetic resonance imaging scanner
         - A type of device used for magnetic resonance imaging.
       * - MRI scanner
         - An 'MRI scanner' is a machine that uses strong magnetic fields, magnetic field gradients, and radio waves to generate static or time-resolved three-dimensional images of the anatomy and physiological processes of the body.
       * - microscope
         - A 'microscope' is an instrument used to obtain a magnified image of small objects and reveal details of structures not otherwise distinguishable.
       * - microtome
         - A 'microtome' is a mechanical instrument with a steel, glass or diamond blade used to cut (typically) biological specimens into very thin segments for further treatment and ultimately microscopic or histologic examination.
       * - electronic amplifier
         - An 'electronic amplifier' is a device that increases the power (voltage or current) of a time-varying signal.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base_v3 import KGObject, IRI
from fairgraph.fields import Field




class DeviceType(KGObject):
    """


    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - vibrating microtome
         - A 'vibrating microtome' is an mechanical instrument with a vibrating steel blade used to cut (typically) biological specimens into thin segments for further treatment and ultimately microscopic or histologic examination.
       * - CT scanner
         - A 'CT scanner' is an x-ray machine that creates and combines serial two-dimensional x-ray images (sections) with the aid of a computer to generate cross-sectional views and/or three-dimensional images of internal body structures (e.g., bones, blood vessels or soft tissues).
       * - magnetic resonance imaging scanner
         - A type of device used for magnetic resonance imaging.
       * - MRI scanner
         - An 'MRI scanner' is a machine that uses strong magnetic fields, magnetic field gradients, and radio waves to generate static or time-resolved three-dimensional images of the anatomy and physiological processes of the body.
       * - microscope
         - A 'microscope' is an instrument used to obtain a magnified image of small objects and reveal details of structures not otherwise distinguishable.
       * - microtome
         - A 'microtome' is a mechanical instrument with a steel, glass or diamond blade used to cut (typically) biological specimens into very thin segments for further treatment and ultimately microscopic or histologic examination.
       * - electronic amplifier
         - An 'electronic amplifier' is a device that increases the power (voltage or current) of a time-varying signal.

    """
    default_space = "controlled"
    type = ["https://openminds.ebrains.eu/controlledTerms/DeviceType"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the device type."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the device type."),
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
