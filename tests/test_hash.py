'''
File:          test_hash.py
File Created:  2022-10-06 15:16:37
Author:        callmexss (callmexss@126.com)
Description:   test code for hash.py
'''

import pathlib

from pyhandy import hashtool


curdir = pathlib.Path(__file__).parent


def test_empty_hash():
    assert hashtool.md5sum() == "d41d8cd98f00b204e9800998ecf8427e"

    with open(curdir / "empty.txt", "w") as f:
        pass

    assert hashtool.md5sum(curdir / "empty.txt") == "d41d8cd98f00b204e9800998ecf8427e"