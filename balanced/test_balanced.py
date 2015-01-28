from balanced import is_balanced


def test_is_balanced():
    assert is_balanced("( ( ) )")
    assert is_balanced("( { } )")
    assert is_balanced("[ ( [ { } ] ) ]")


def test_is_not_balanced():
    assert not is_balanced("(")
    assert not is_balanced("( { ) }")
    assert not is_balanced("[ { ( ( ) } ) ]")
    assert not is_balanced("( ( )")
    assert not is_balanced("( ) )")

