import datetime

import pytest
from openminds import IRI
import fairgraph.openminds.core as omcore
import fairgraph.openminds.publications as ompub
from fairgraph.kgproxy import KGProxy
from fairgraph.caching import object_cache
from fairgraph.utility import as_list

from test.utils import kg_client, skip_if_no_connection, mock_client, clear_caches, MockKGResponse
from fairgraph.queries import get_filter_value
from openminds.properties import Property


def test_get_journal():
    jphysiol = ompub.Periodical(name="The Journal of Physiology")
    volume = ompub.PublicationVolume(is_part_of=jphysiol, volume_number="117")
    issue = ompub.PublicationIssue(is_part_of=volume, issue_number="4")
    article = ompub.ScholarlyArticle(
        name="A quantitative description of membrane current and its application to conduction and excitation in nerve",
        authors=[
            omcore.Person(given_name="AL", family_name="Hodgkin"),
            omcore.Person(given_name="AF", family_name="Huxley"),
        ],
        is_part_of=issue,
        publication_date=datetime.date(1952, 8, 1),
        pagination="500–44",
    )
    assert article.get_journal(client=None) == jphysiol
    assert article.get_journal(client=None, with_volume=True) == (jphysiol, volume)
    assert article.get_journal(client=None, with_volume=True, with_issue=True) == (jphysiol, volume, issue)

    expected = "AL Hodgkin & AF Huxley (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. The Journal of Physiology, 117: 500–44."
    assert article.get_citation_string(client=None) == expected


def test_get_journal_with_issue_proxy_journal():
    """When data comes from the KG, volume.is_part_of is a KGProxy, not a resolved Periodical.
    get_journal() should resolve the proxy rather than failing the isinstance assertion."""
    periodical_id = "https://kg.ebrains.eu/api/instances/00000000-0000-0000-0000-000000000001"
    jphysiol = ompub.Periodical(name="The Journal of Physiology", id=periodical_id)
    object_cache[periodical_id] = jphysiol

    try:
        journal_proxy = KGProxy(ompub.Periodical, periodical_id)
        volume = ompub.PublicationVolume(is_part_of=journal_proxy, volume_number="117")
        issue = ompub.PublicationIssue(is_part_of=volume, issue_number="4")
        article = ompub.ScholarlyArticle(
            name="A quantitative description of membrane current and its application to conduction and excitation in nerve",
            authors=[
                omcore.Person(given_name="AL", family_name="Hodgkin"),
                omcore.Person(given_name="AF", family_name="Huxley"),
            ],
            is_part_of=issue,
            publication_date=datetime.date(1952, 8, 1),
            pagination="500–44",
        )
        assert article.get_journal(client=None) == jphysiol
        assert article.get_journal(client=None, with_volume=True) == (jphysiol, volume)
        assert article.get_journal(client=None, with_volume=True, with_issue=True) == (jphysiol, volume, issue)
    finally:
        del object_cache[periodical_id]


def test_get_journal_no_issue():
    jphysiol = ompub.Periodical(name="The Journal of Physiology")
    volume = ompub.PublicationVolume(is_part_of=jphysiol, volume_number="117")
    article = ompub.ScholarlyArticle(
        name="A quantitative description of membrane current and its application to conduction and excitation in nerve",
        authors=[
            omcore.Person(given_name="AL", family_name="Hodgkin"),
            omcore.Person(given_name="AF", family_name="Huxley"),
        ],
        is_part_of=volume,
        publication_date=datetime.date(1952, 8, 1),
        pagination="500–44",
    )
    assert article.get_journal(client=None) == jphysiol
    assert article.get_journal(client=None, with_volume=True) == (jphysiol, volume)
    assert article.get_journal(client=None, with_volume=True, with_issue=True) == (jphysiol, volume, None)

    expected = "AL Hodgkin & AF Huxley (1952). A quantitative description of membrane current and its application to conduction and excitation in nerve. The Journal of Physiology, 117: 500–44."
    assert article.get_citation_string(client=None) == expected


@pytest.mark.parametrize("value,expected", [
    ("1937-09-21", "1937-09-21"),
    ("not-a-date", None),
    ("1937-02-31", None),
    ("1937-09-21T12:00:00", None),
])
def test_date_filter_accepts_only_iso_dates(value, expected):
    prop = next(prop for prop in ompub.Book.properties if prop.name == "publication_date")
    if expected is None:
        with pytest.raises(TypeError):
            get_filter_value(prop, value)
    else:
        assert get_filter_value(prop, value) == expected


@pytest.mark.parametrize("value,expected", [
    ("1937-09-21T12:00:00", "1937-09-21T12:00:00"),
    ("1937-09-21", "1937-09-21"),
    ("1937-02-31T12:00:00", None),
    ("not-a-datetime", None),
])
def test_datetime_filter_accepts_only_iso_datetimes(value, expected):
    prop = Property("timestamp", datetime.datetime, "https://openminds.om-i.org/props/timestamp")
    if expected is None:
        with pytest.raises(TypeError):
            get_filter_value(prop, value)
    else:
        assert get_filter_value(prop, value) == expected


def test_new_book_with_date_is_saved(mock_client, clear_caches, mocker):
    book = ompub.Book(name="The Hobbit", publication_date=datetime.date(1937, 9, 21))
    query = mocker.patch.object(mock_client, "query", return_value=MockKGResponse([]))
    book.save(mock_client, space="myspace_1234", recursive=False)
    assert query.call_count == 1
    assert len(mock_client.instances) == 1
    assert next(iter(mock_client.instances.values()))["https://openminds.om-i.org/props/publicationDate"] == "1937-09-21"


@skip_if_no_connection
def test_filter_on_iri(kg_client):
    # test that filtering by IRI accepts string values, even though the value itself is an IRI object
    tutorial_notebooks = as_list(ompub.LearningResource.list(kg_client, size=20, iri="ipynb"))
    assert len(tutorial_notebooks) > 10
    assert all(isinstance(nb.iri, IRI) for nb in tutorial_notebooks)
    assert all("ipynb" in str(nb.iri) for nb in tutorial_notebooks)
