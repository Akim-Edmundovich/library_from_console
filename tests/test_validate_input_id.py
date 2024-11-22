import pytest

from app import validate_input_id

data_for_testing = [
    (1, 1),
    ('1', 1),
    ('abc', False),
    ('', False),
    (None, False),
    ('$%^', False),
]


@pytest.mark.parametrize(
    'data',
    data_for_testing
)
def test_input_data(data):
    inp, out = data
    assert validate_input_id(inp) == out
