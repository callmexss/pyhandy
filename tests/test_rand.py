"""
File:          random_handy_test.py
File Created:  2022-10-05 20:24:31
Author:        callmexss (callmexss@126.com)
Description:   test code for rand.py
"""


import random
import string

import pytest

from pyhandy import rand


FIXED_RAND = rand.RandomHandy(random.Random(0))


def test_init():
    with pytest.raises(TypeError):
        rand.RandomHandy(123)


@pytest.mark.parametrize("n", [0, 1, 3, 50])
def test_size(n):
    li = FIXED_RAND.generate_num_list(n)
    assert len(li) == n


def test_size_out_of_scope():
    with pytest.raises(ValueError):
        FIXED_RAND.generate_num_list(1e4)


@pytest.mark.parametrize("n", [1, 3, 10, 100])
def test_unique(n):
    li = FIXED_RAND.generate_num_list(n)
    assert len(set(li)) == len(li)


@pytest.mark.parametrize("n", [1, 3, 10, 100])
def test_int(n):
    li = FIXED_RAND.generate_num_list(n)
    assert all(map(lambda x: isinstance(x, int), li))
    arr = FIXED_RAND.generate_int_array(n)
    assert all(map(lambda x: isinstance(x, int), arr))


@pytest.mark.parametrize("n", [1, 3, 10, 100])
def test_float(n):
    li = FIXED_RAND.generate_num_list(n, element_type=float)
    assert all(map(lambda x: isinstance(x, float), li))


@pytest.mark.parametrize("n", [0, 1, 3, 52])
def test_string_size(n):
    s = FIXED_RAND.generate_string(n)
    assert len(s) == n


@pytest.mark.parametrize("n", [0, 1, 3, 52])
def test_unique_string_with_sufficient_provider(n):
    s = FIXED_RAND.generate_string(n, True, string.ascii_letters)
    assert len(set(s)) == n


def test_unique_string_with_insufficient_provider():
    with pytest.raises(ValueError):
        FIXED_RAND.generate_string(50, True, string.ascii_letters)
