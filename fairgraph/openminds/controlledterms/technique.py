"""
Structured information on the technique.
    Here we show the first 20 possible values, an additional 277 values are not shown.

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

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class Technique(KGObject):
    """
    Structured information on the technique.
    Here we show the first 20 possible values, an additional 277 values are not shown.

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

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/Technique"]
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
            doc="Word or phrase that constitutes the distinctive designation of the technique.",
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
            doc="Longer statement or account giving the characteristics of the technique.",
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
            "is_reference_for",
            "openminds.computation.ValidationTest",
            "^vocab:referenceDataAcquisition",
            reverse="reference_data_acquisitions",
            multiple=True,
            doc="reverse of 'referenceDataAcquisition'",
        ),
        Field(
            "is_used_to_group",
            "openminds.core.FileBundle",
            "^vocab:groupedBy",
            reverse="grouped_by",
            multiple=True,
            doc="reverse of 'groupedBy'",
        ),
        Field(
            "used_in",
            "openminds.core.Protocol",
            "^vocab:technique",
            reverse="techniques",
            multiple=True,
            doc="reverse of 'technique'",
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
        is_reference_for=None,
        is_used_to_group=None,
        used_in=None,
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
            is_reference_for=is_reference_for,
            is_used_to_group=is_used_to_group,
            used_in=used_in,
        )
