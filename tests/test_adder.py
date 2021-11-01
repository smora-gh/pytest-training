from proj.adder import adder
import pytest


def test_adder():
    assert adder(1, 2) == 3


def test_exc():
    with pytest.raises(TypeError):
        adder("", 3)
