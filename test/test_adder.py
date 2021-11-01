from proj.adder import adder


def test_adder(x, y):
    x = adder(1, 2)
    assert x == 3
