"""
Structured information on the technique.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - independent component analysis
         -
       * - mass spectrometry
         -
       * - current step stimulation
         - Current step stimulation is a technique in which an amount of current is applied in predefined steps, whilst measuring changes in neural/muscular activity.
       * - stochastic online matrix factorization
         - 'Stochastic online matrix factorization' is a matrix-factorization algorithm that scales to input matrices with both huge number of rows and columns [(Mensch et al., 2018)](https://doi.org/10.1109/TSP.2017.2752697).
       * - semiquantitative analysis
         - An analysis technique which constitutes or involves less than quantitative precision.
       * - `light sheet fluorescence microscopy <http://uri.interlex.org/tgbugs/uris/readable/technique/lightSheetMicroscopyFluorescent>`_
         - Lightsheet fluorescence microscopy is a fluorescence microscopy technique that uses a thin sheet of light to excite only fluorophores within the plane of illumination.
       * - beta-galactosidase staining
         -
       * - TDE clearing
         -
       * - anaesthesia technique
         -
       * - anatomical delineation technique
         -
       * - density measurement
         -
       * - time-of-flight magnetic resonance angiography
         - 'Time-of-flight magnetic resonance angiography' is a non-invasive, non-contrast-enhanced technique used to visualize both arterial and venous vessels with high spatial resolution. Note: it provides no information regarding directionality nor flow velocity quantification. [adapted from:  [Ferreira and Ramalho, 2013](https://doi.org/10.1002/9781118434550.ch7)]
       * - ultra high-field magnetic resonance imaging
         - 'Ultra high-field magnetic resonance imaging' comprises all structural MRI techniques conducted with a MRI scanner with a magnetic field strength equal or above 7 Tesla.
       * - optogenetic stimulation
         - Using light of a particular wavelength, 'optogenetic stimulation' increases or inhibits the activity of neuron populations that express (typically due to genetic manipulation) light-sensitive ion channels, pumps or enzymes.
       * - nonrigid image registration
         - A 'nonrigid image registration' is a process of bringing a set of images into the same coordinate system using nonrigid transformation.
       * - electrooculography
         -
       * - metadata parsing
         -
       * - transformation
         - A 'transformation' is a mathematical function to map coordinates between two different coordinate systems.
       * - `electron tomography <http://id.nlm.nih.gov/mesh/2018/M0512939>`_
         - Electron tomography is a microscopy technique that takes a series of images of a thick sample at different angles (tilts) so that tomography can be applied to increase the resolution of the ticker sample.
       * - ultra high-field functional magnetic resonance imaging
         - 'Ultra high-field functional magnetic resonance imaging' comprises all functional MRI techniques conducted with a MRI scanner with a magnetic field strength equal or above 7 Tesla.

Here we show the first 20 values, an additional 275 values are not shown.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph.base import KGObject, IRI
from fairgraph.fields import Field




class Technique(KGObject):
    """
    Structured information on the technique.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - independent component analysis
         -
       * - mass spectrometry
         -
       * - current step stimulation
         - Current step stimulation is a technique in which an amount of current is applied in predefined steps, whilst measuring changes in neural/muscular activity.
       * - stochastic online matrix factorization
         - 'Stochastic online matrix factorization' is a matrix-factorization algorithm that scales to input matrices with both huge number of rows and columns [(Mensch et al., 2018)](https://doi.org/10.1109/TSP.2017.2752697).
       * - semiquantitative analysis
         - An analysis technique which constitutes or involves less than quantitative precision.
       * - `light sheet fluorescence microscopy <http://uri.interlex.org/tgbugs/uris/readable/technique/lightSheetMicroscopyFluorescent>`_
         - Lightsheet fluorescence microscopy is a fluorescence microscopy technique that uses a thin sheet of light to excite only fluorophores within the plane of illumination.
       * - beta-galactosidase staining
         -
       * - TDE clearing
         -
       * - anaesthesia technique
         -
       * - anatomical delineation technique
         -
       * - density measurement
         -
       * - time-of-flight magnetic resonance angiography
         - 'Time-of-flight magnetic resonance angiography' is a non-invasive, non-contrast-enhanced technique used to visualize both arterial and venous vessels with high spatial resolution. Note: it provides no information regarding directionality nor flow velocity quantification. [adapted from:  [Ferreira and Ramalho, 2013](https://doi.org/10.1002/9781118434550.ch7)]
       * - ultra high-field magnetic resonance imaging
         - 'Ultra high-field magnetic resonance imaging' comprises all structural MRI techniques conducted with a MRI scanner with a magnetic field strength equal or above 7 Tesla.
       * - optogenetic stimulation
         - Using light of a particular wavelength, 'optogenetic stimulation' increases or inhibits the activity of neuron populations that express (typically due to genetic manipulation) light-sensitive ion channels, pumps or enzymes.
       * - nonrigid image registration
         - A 'nonrigid image registration' is a process of bringing a set of images into the same coordinate system using nonrigid transformation.
       * - electrooculography
         -
       * - metadata parsing
         -
       * - transformation
         - A 'transformation' is a mathematical function to map coordinates between two different coordinate systems.
       * - `electron tomography <http://id.nlm.nih.gov/mesh/2018/M0512939>`_
         - Electron tomography is a microscopy technique that takes a series of images of a thick sample at different angles (tilts) so that tomography can be applied to increase the resolution of the ticker sample.
       * - ultra high-field functional magnetic resonance imaging
         - 'Ultra high-field functional magnetic resonance imaging' comprises all functional MRI techniques conducted with a MRI scanner with a magnetic field strength equal or above 7 Tesla.

Here we show the first 20 values, an additional 275 values are not shown.

    """
    default_space = "controlled"
    type = ["https://openminds.ebrains.eu/controlledTerms/Technique"]
    context = {
        "schema": "http://schema.org/",
        "kg": "https://kg.ebrains.eu/api/instances/",
        "vocab": "https://openminds.ebrains.eu/vocab/",
        "terms": "https://openminds.ebrains.eu/controlledTerms/",
        "core": "https://openminds.ebrains.eu/core/"
    }
    fields = [
        Field("name", str, "vocab:name", multiple=False, required=True,
              doc="Word or phrase that constitutes the distinctive designation of the technique."),
        Field("definition", str, "vocab:definition", multiple=False, required=False,
              doc="Short, but precise statement of the meaning of a word, word group, sign or a symbol."),
        Field("description", str, "vocab:description", multiple=False, required=False,
              doc="Longer statement or account giving the characteristics of the technique."),
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
