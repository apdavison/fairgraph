import sys
from fairgraph.openminds import (
    list_kg_classes as _lkgc,
    list_embedded_metadata_classes as _lemc,
    set_error_handling as _seh,
)

from .book import Book
from .chapter import Chapter
from .learning_resource import LearningResource
from .live_paper import LivePaper
from .live_paper_resource_item import LivePaperResourceItem
from .live_paper_section import LivePaperSection
from .live_paper_version import LivePaperVersion
from .periodical import Periodical
from .publication_issue import PublicationIssue
from .publication_volume import PublicationVolume
from .scholarly_article import ScholarlyArticle


def list_kg_classes():
    """List all KG classes defined in this module"""
    return _lkgc(sys.modules[__name__])


def list_embedded_metadata_classes():
    """List all embedded metadata classes defined in this module"""
    return _lemc(sys.modules[__name__])


def set_error_handling(value):
    """
    Control validation for all classes in this module.

    Args:
        value (str): action to follow when there is a validation failure.
            (e.g. if a required property is not provided).
            Possible values: "error", "warning", "log", None
    """
    _seh(value, sys.modules[__name__])
