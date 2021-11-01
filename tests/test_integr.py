from _pytest.python_api import raises
import pytest
from proj.integr import parse

# import pytest


def test_parse():
    s = parse("1,2,3,4")
    assert isinstance(s, list) and s == [1, 2, 3, 4], "should be list of int"


def test_bad1():
    with pytest.raises(ValueError):
        parse("bad input")


@pytest.mark.xfail(raises=ValueError)
def test_bad2():
    assert parse("1-3, 12-15")
