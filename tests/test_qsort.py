import random

import pytest

from rdp_testcase.testcase1.sort import qsort


@pytest.fixture
def get_array():
    return random.sample(range(-100, 100), 100)


def test_qsort(get_array):
    assert sorted(get_array) == qsort(get_array)
