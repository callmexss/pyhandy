'''
File:          test_context.py
File Created:  2022-10-06 15:39:27
Author:        callmexss (callmexss@126.com)
Description:   test code for context.py
'''

from pathlib import Path

from pyhandy import context


curdir = Path(__file__).parent


def test_checker():
    with context.Checker(curdir / "test_checker.txt") as checker:
        checker.insert("aaa")
        checker.insert("bbb")
    assert context.load_set(curdir / "test_checker.txt") == {"aaa", "bbb"}