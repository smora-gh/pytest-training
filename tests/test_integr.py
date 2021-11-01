from Integer.integr import parse


def test_basic():
    s = parse("1,2,3,4")
    assert isinstance(s, list)
