from fairgraph.registry import Registry
from fairgraph.fields import Field


def test_docstring_generation():
    class Foo(metaclass=Registry):
        """This is the base docstring"""

        fields = [Field("foo", str, "Foo", doc="foo-foo")]

    assert Foo.__doc__ == "\nThis is the base docstring\n\nArgs\n----\nfoo : str\n    foo-foo\n\n"
