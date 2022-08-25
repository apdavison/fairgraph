import sys
import inspect
from ...base_v3 import KGObject

from .publication_issue import PublicationIssue
from .book import Book
from .live_paper_section import LivePaperSection
from .periodical import Periodical
from .chapter import Chapter
from .live_paper_version import LivePaperVersion
from .publication_volume import PublicationVolume
from .live_paper_resource_item import LivePaperResourceItem
from .live_paper import LivePaper
from .scholarly_article import ScholarlyArticle


def list_kg_classes():
    """List all KG classes defined in this module"""
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__])
           if inspect.isclass(obj) and issubclass(obj, KGObject) and obj.__module__.startswith(__name__)]
