from openminds.properties import Property

from fairgraph.registry import Node


def test_docstring_generation():
    class Foo(metaclass=Node):
        """This is the base docstring"""

        properties = [Property("foo", str, "Foo", doc="foo-foo")]

    assert Foo.__doc__ == "\nThis is the base docstring\n\nArgs\n----\nfoo : str\n    foo-foo\n\n"
