import random

import pytest

from rdp_testcase.testcase1.sort import qsort


@pytest.fixture
def get_list():
    return random.sample(range(-100, 100), 100)


def test_qsort(get_list):
    assert sorted(get_list) == qsort(get_list)

def test_one_element_list():
    assert [1] == qsort([1])