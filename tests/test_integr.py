from proj.integr import parse


def test_parse():
    s = parse("1,2,3,4")
    assert isinstance(s, list)
