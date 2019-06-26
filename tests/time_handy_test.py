'''
File:          time_handy_test.py
File Created:  Wednesday, 26th June 2019 11:16:01 am
Author:        xss (callmexss@126.com)
Description:   time handy tools test
-----
Last Modified: Wednesday, 26th June 2019 11:16:18 am
Modified By:   xss (callmexss@126.com)
-----
'''

import unittest
import time

import __init__
import pyhandy.pyhandy as handy


class TestTimeHandy(unittest.TestCase):
    def test_time_handy(self):
        now = time.time()
        fmt_time = handy.TimeHandy.get_format_time(now)

        self.assertEqual(handy.TimeHandy.get_epoch_time(fmt_time), float(int(now)))
        self.assertAlmostEqual(handy.TimeHandy.get_epoch_time(fmt_time), now, delta=1)

if __name__ == '__main__':
    unittest.main()
    