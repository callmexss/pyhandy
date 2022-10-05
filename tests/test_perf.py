'''
File:          test_perf.py
File Created:  2022-10-05 20:24:31
Author:        callmexss (callmexss@126.com)
Description:   test code for perf.py
'''

import pytest

from pyhandy import perf


@pytest.mark.parametrize("epoch_time, fmt, format_time", [
    (1234567890, "%Y-%m-%d %H:%M:%S", '2009-02-14 07:31:30'),
    (1234567890, "%Y-%m-%d", '2009-02-14'),
    (1234567890, "%H:%M:%S", '07:31:30'),
])
def test_get_format_time(epoch_time, fmt, format_time):
    assert perf.TimeHandy.get_format_time(epoch_time, fmt) == format_time