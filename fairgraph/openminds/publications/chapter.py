"""
<description not available>
"""

# this file was auto-generated

from openminds.properties import Property
from openminds.latest.publications import Chapter as OMChapter
from fairgraph import KGObject


from datetime import date
from openminds import IRI


class Chapter(KGObject, OMChapter):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Chapter"
    default_space = "livepapers"
    # forward properties are defined in the parent class (in openMINDS-Python)
    reverse_properties = [
        Property(
            "related_to",
            [
                "openminds.latest.computation.ValidationTestVersion",
                "openminds.latest.computation.WorkflowRecipeVersion",
                "openminds.latest.core.DatasetVersion",
                "openminds.latest.core.MetaDataModelVersion",
                "openminds.latest.core.ModelVersion",
                "openminds.latest.core.SoftwareVersion",
                "openminds.latest.core.WebServiceVersion",
                "openminds.latest.publications.LivePaperVersion",
                "openminds.latest.sands.BrainAtlasVersion",
                "openminds.latest.sands.CommonCoordinateSpaceVersion",
            ],
            "relatedPublication",
            reverse="related_publications",
            multiple=True,
            description="reverse of 'related_publications'",
        ),
    ]
    existence_query_properties = ("authors", "is_part_of", "name", "publication_date")

    def __init__(
        self,
        name=None,
        abstract=None,
        authors=None,
        cited_publications=None,
        copyright=None,
        creation_date=None,
        custodians=None,
        digital_identifier=None,
        editors=None,
        funding=None,
        iri=None,
        is_part_of=None,
        keywords=None,
        license=None,
        modification_date=None,
        pagination=None,
        publication_date=None,
        publisher=None,
        related_to=None,
        version_identifier=None,
        id=None,
        data=None,
        space=None,
        scope=None,
    ):
        return KGObject.__init__(
            self,
            id=id,
            space=space,
            scope=scope,
            data=data,
            name=name,
            abstract=abstract,
            authors=authors,
            cited_publications=cited_publications,
            copyright=copyright,
            creation_date=creation_date,
            custodians=custodians,
            digital_identifier=digital_identifier,
            editors=editors,
            funding=funding,
            iri=iri,
            is_part_of=is_part_of,
            keywords=keywords,
            license=license,
            modification_date=modification_date,
            pagination=pagination,
            publication_date=publication_date,
            publisher=publisher,
            related_to=related_to,
            version_identifier=version_identifier,
        )


# cast openMINDS instances to their fairgraph subclass
Chapter.set_error_handling(None)
for key, value in OMChapter.__dict__.items():
    if isinstance(value, OMChapter):
        fg_instance = Chapter.from_jsonld(value.to_jsonld())
        fg_instance._space = Chapter.default_space
        setattr(Chapter, key, fg_instance)
Chapter.set_error_handling("log")
