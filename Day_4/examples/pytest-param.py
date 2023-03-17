import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("test_input, expected_output", [
    ((1, 2), 3),
    ((-1, 1), 0),
    (("hello", "world"), "helloworld"),
    (([1, 2, 3], [4, 5]), [1, 2, 3, 4, 5]),
    (([], []), []),
])
def test_addition(test_input, expected_output):
    assert add(*test_input) == expected_output