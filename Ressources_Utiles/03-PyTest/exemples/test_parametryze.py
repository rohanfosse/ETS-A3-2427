import pytest
from calcul import addition

@pytest.mark.parametrize("a, b, attendu", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (10, -5, 5)
])
def test_addition(a, b, attendu):
    assert addition(a, b) == attendu
