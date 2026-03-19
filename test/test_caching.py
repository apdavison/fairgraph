# encoding: utf-8
"""
Tests for fairgraph.caching module.
"""

import pytest
from fairgraph.caching import generate_cache_key, object_cache, save_cache


class TestGenerateCacheKey:

    def test_raises_on_non_dict(self):
        with pytest.raises(TypeError):
            generate_cache_key(None)

    def test_raises_on_non_dict_string(self):
        with pytest.raises(TypeError):
            generate_cache_key("not a dict")

    def test_simple_string_values_sorted(self):
        result = generate_cache_key({"b": "two", "a": "one"})
        assert result == (("a", "one"), ("b", "two"))

    def test_int_value(self):
        result = generate_cache_key({"x": 42})
        assert result == (("x", 42),)

    def test_float_value(self):
        result = generate_cache_key({"y": 3.14})
        assert result == (("y", 3.14),)

    def test_list_of_scalars(self):
        # list branch with non-dict sub-values: str(value) is used
        result = generate_cache_key({"k": ["foo", "bar"]})
        assert isinstance(result, tuple)
        assert len(result) == 1
        # the tuple inside should have one entry (the sub_key tuple)
        inner = result[0]
        assert isinstance(inner, tuple)

    def test_list_of_dicts(self):
        # recursive call branch
        result = generate_cache_key({"k": [{"a": "1"}, {"b": "2"}]})
        assert isinstance(result, tuple)

    def test_nested_dict_value(self):
        # isinstance(value, dict) branch
        result = generate_cache_key({"k": {"inner": "val"}})
        assert isinstance(result, tuple)
        assert result[0][0] == "k"
        assert "inner" in result[0][1]

    def test_iri_value(self):
        # __class__.__name__ == "IRI" branch
        FakeIRI = type("IRI", (), {"__str__": lambda self: "https://example.com/iri"})
        iri = FakeIRI()
        result = generate_cache_key({"k": iri})
        assert result == (("k", "https://example.com/iri"),)

    def test_raises_on_invalid_value_type(self):
        with pytest.raises(TypeError):
            generate_cache_key({"k": object()})

    def test_empty_dict(self):
        result = generate_cache_key({})
        assert result == ()


def test_object_cache_is_dict():
    assert isinstance(object_cache, dict)


def test_save_cache_is_dict():
    assert isinstance(save_cache, dict)
