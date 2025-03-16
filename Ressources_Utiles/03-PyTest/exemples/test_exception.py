import pytest
from Utils.PyTest.exemples.operations import division

def test_division():
    assert division(10, 2) == 5
    assert division(9, 3) == 3

    with pytest.raises(ValueError):
        division(10, 0)  # Doit lever une erreur
