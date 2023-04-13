from datetime import date
from uuid import uuid4
from fairgraph.fields import Field
from fairgraph.kgobject import KGObject
from fairgraph.embedded import EmbeddedMetadata
from fairgraph.kgproxy import KGProxy
import pytest


class SomeOrganization(KGObject):
    default_space = "common"
    type_ = ["https://openminds.ebrains.eu/test/Organization"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/",
    }
    fields = [
        Field("name", str, "vocab:fullName", multiple=False, required=True),
        Field("alias", str, "vocab:shortName", multiple=False, required=False),
    ]
    existence_query_fields = ("name",)


class SomeAffiliation(EmbeddedMetadata):
    type_ = ["https://openminds.ebrains.eu/test/Affiliation"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/",
    }
    fields = [
        Field("end_date", date, "vocab:endDate", multiple=False, required=False),
        Field("member_of", (SomeOrganization,), "vocab:memberOf", multiple=False, required=False),
        Field("start_date", date, "vocab:startDate", multiple=False, required=False),
    ]


class SomeContactInformation(KGObject):
    default_space = "restricted"
    type_ = ["https://openminds.ebrains.eu/test/ContactInformation"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/",
    }
    fields = [Field("email", str, "vocab:email", multiple=False, required=True)]
    existence_query_fields = ("email",)


def test_serialize_embedded():
    field_embedded_metadata = Field(
        "affiliations", (SomeAffiliation,), "vocab:affiliation", multiple=True, required=False
    )

    client = None
    test_affiliation = SomeAffiliation(
        start_date=date(2023, 1, 1),
        member_of=SomeOrganization(
            name="Acme Corporation",
            alias="acme",
            id=f"https://kg.ebrains.eu/api/instances/{uuid4()}",
        ),
    )
    result = field_embedded_metadata.serialize(test_affiliation, follow_links=False)
    expected = {
        "@type": SomeAffiliation.type_,
        "https://openminds.ebrains.eu/vocab/memberOf": {"@id": test_affiliation.member_of.id},
        "https://openminds.ebrains.eu/vocab/startDate": "2023-01-01",
    }
    assert result == expected


def test_serialize_no_multiple():
    field_no_multiple = Field(
        "contact_information",
        (SomeContactInformation,),
        "vocab:contactInformation",
        multiple=False,
        required=False,
        strict=True,
    )
    client = None

    # single object
    test_info = SomeContactInformation(
        email="someone@example.com", id=f"https://kg.ebrains.eu/api/instances/{uuid4()}"
    )
    result = field_no_multiple.serialize(test_info, follow_links=False)
    expected = {"@id": test_info.id}
    assert result == expected

    # single proxy
    test_info = KGProxy(SomeContactInformation, f"https://kg.ebrains.eu/api/instances/{uuid4()}")
    result = field_no_multiple.serialize(test_info, follow_links=False)
    expected = {"@id": test_info.id}
    assert result == expected

    # two objects, strict
    test_info = [
        SomeContactInformation(email="someone@example.com", id=f"https://kg.ebrains.eu/api/instances/{uuid4()}"),
        SomeContactInformation(email="sameperson@example.com", id=f"https://kg.ebrains.eu/api/instances/{uuid4()}"),
    ]
    with pytest.raises(AttributeError):
        result = field_no_multiple.serialize(test_info, follow_links=False)

    # two objects, not strict
    field_no_multiple.strict_mode = False
    test_info = [
        SomeContactInformation(email="someone@example.com", id=f"https://kg.ebrains.eu/api/instances/{uuid4()}"),
        SomeContactInformation(email="sameperson@example.com", id=f"https://kg.ebrains.eu/api/instances/{uuid4()}"),
    ]
    result = field_no_multiple.serialize(test_info, follow_links=False)
    expected = [{"@id": test_info[0].id}, {"@id": test_info[1].id}]
    assert result == expected

    # two proxies, not strict
    field_no_multiple.strict_mode = False
    test_info = [
        KGProxy(SomeContactInformation, f"https://kg.ebrains.eu/api/instances/{uuid4()}"),
        KGProxy(SomeContactInformation, f"https://kg.ebrains.eu/api/instances/{uuid4()}"),
    ]
    result = field_no_multiple.serialize(test_info, follow_links=False)
    expected = [{"@id": test_info[0].id}, {"@id": test_info[1].id}]
    assert result == expected
