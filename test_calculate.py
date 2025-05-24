import pytest
from calculate import calculate_area


def test_area_positive():
    assert calculate_area(3, 4) == 12


def test_area_zero():
    assert calculate_area(0, 5) == 0


def test_area_negative():
    with pytest.raises(ValueError):
        calculate_area(-1, 5)
