import pytest


@pytest.mark.utest
def test_it_should_confirm_variable_of_type_list():
    num_range: list = list(range(10))
    assert type(num_range) is list

