'''
File:          random_worker_test.py
File Created:  Wednesday, 19th June 2019 6:06:09 pm
Author:        xss (callmexss@126.com)
Description:   test random worker
-----
Last Modified: Wednesday, 19th June 2019 6:06:12 pm
Modified By:   xss (callmexss@126.com)
-----
'''

import sys
import doctest
import unittest

import __init__
import pyhandy.pyhandy as handy


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        e = arr[i]
        j = i
        while j > 0 and arr[j - 1] > e:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = e

class TestRandomWorker(unittest.TestCase):
    def setup(self):
        self.worker = handy.RandomHandy()
    

if __name__ == '__main__':
    random_handy = handy.RandomHandy()
    sort_handy = handy.SortHandy()

    # li = worker.gen_list(10000, (0, 100000))
    li = random_handy.generate_nearly_ordered_array(100, 10)
    li1 = li[:]
    sort_handy.testSort(selection_sort, li)
    sort_handy.testSort(insertion_sort, li1)
