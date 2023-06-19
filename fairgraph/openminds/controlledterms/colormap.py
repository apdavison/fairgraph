"""

    Here we show the first 20 possible values, an additional 63 values are not shown.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - matplotlib.colormaps.Set2
         - The colormap 'Set2' is a qualitative colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.magma
         - The colormap 'magma' is a perceptually uniform sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.summer
         - The colormap 'summer' is a sequential (type 2) colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.RdPu
         - The colormap 'RdPu' is a sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.cubehelix
         - The colormap 'cubehelix' is a miscellaneous colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.plasma
         - The colormap 'plasma' is a perceptually uniform sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.gist_rainbow
         - The colormap 'gist_rainbow' is a miscellaneous colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.gnuplot2
         - The colormap 'gnuplot2' is a miscellaneous colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.turbo
         - The colormap 'turbo' is a miscellaneous colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.YlGnBu
         - The colormap 'YlGnBu' is a sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.CMRmap
         - The colormap 'CMRmap' is a miscellaneous colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.PuBuGn
         - The colormap 'PuBuGn' is a sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.jet
         - The colormap 'jet' is a miscellaneous colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.YlOrBr
         - The colormap 'YlOrBr' is a sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.tab20b
         - The colormap 'tab20b' is a qualitative colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.YlGn
         - The colormap 'YlGn' is a sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.Accent
         - The colormap 'Accent' is a qualitative colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.inferno
         - The colormap 'inferno' is a perceptually uniform sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.RdYlBu
         - The colormap 'RdYlBu' is a diverging colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.PuOr
         - The colormap 'PuOr' is a diverging colormap of the Python plotting library Matplotlib.

"""

# this file was auto-generated

from datetime import date, datetime
from fairgraph import KGObject, IRI
from fairgraph.fields import Field


class Colormap(KGObject):
    """

    Here we show the first 20 possible values, an additional 63 values are not shown.

    .. list-table:: **Possible values**
       :widths: 20 80
       :header-rows: 0

       * - matplotlib.colormaps.Set2
         - The colormap 'Set2' is a qualitative colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.magma
         - The colormap 'magma' is a perceptually uniform sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.summer
         - The colormap 'summer' is a sequential (type 2) colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.RdPu
         - The colormap 'RdPu' is a sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.cubehelix
         - The colormap 'cubehelix' is a miscellaneous colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.plasma
         - The colormap 'plasma' is a perceptually uniform sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.gist_rainbow
         - The colormap 'gist_rainbow' is a miscellaneous colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.gnuplot2
         - The colormap 'gnuplot2' is a miscellaneous colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.turbo
         - The colormap 'turbo' is a miscellaneous colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.YlGnBu
         - The colormap 'YlGnBu' is a sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.CMRmap
         - The colormap 'CMRmap' is a miscellaneous colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.PuBuGn
         - The colormap 'PuBuGn' is a sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.jet
         - The colormap 'jet' is a miscellaneous colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.YlOrBr
         - The colormap 'YlOrBr' is a sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.tab20b
         - The colormap 'tab20b' is a qualitative colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.YlGn
         - The colormap 'YlGn' is a sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.Accent
         - The colormap 'Accent' is a qualitative colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.inferno
         - The colormap 'inferno' is a perceptually uniform sequential colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.RdYlBu
         - The colormap 'RdYlBu' is a diverging colormap of the Python plotting library Matplotlib.
       * - matplotlib.colormaps.PuOr
         - The colormap 'PuOr' is a diverging colormap of the Python plotting library Matplotlib.

    """

    default_space = "controlled"
    type_ = ["https://openminds.ebrains.eu/controlledTerms/Colormap"]
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
            doc="Word or phrase that constitutes the distinctive designation of the colormap.",
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
            doc="Longer statement or account giving the characteristics of the colormap.",
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
        )
