import pytest
from rdp_testcase.testcase1.sort import qsort


@pytest.fixture
def get_array():
    return [10, 1, 2, 56, 34, 2, 3, 7, 9, 99, 234, 75, 45, 888]


def test_qsort(get_array):
    assert qsort(get_array) == [1, 2, 2, 2, 3, 7, 9, 10, 34, 45, 56, 75, 99, 234, 888]
