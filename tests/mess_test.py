import os
import time
import shutil

import __init__

import pyhandy as handy

src_dir = "data"
dst_dir = "2019"
for d in os.listdir(src_dir):
    inner_dir = os.path.join(src_dir, d)
    # print(time.ctime(os.path.getctime(inner_dir)).split()[-1])
    if time.ctime(os.path.getctime(inner_dir)).split()[-1] == "2019":
        try:
            print("{} -> {}".format(inner_dir, os.path.join(dst_dir, d)))
            shutil.copytree(inner_dir, os.path.join(dst_dir, d))
        except Exception as err:
            print(err)