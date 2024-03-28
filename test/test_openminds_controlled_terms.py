import fairgraph.openminds.controlled_terms as terms


def test_initialization():
    for cls in terms.list_kg_classes():
        obj = cls(name="foo")
