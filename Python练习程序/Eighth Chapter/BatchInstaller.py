# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/6 11:40
"""
# BatchInstaller.py

import os

libs = {"numpy", "pillow", "matplotlib", "wordcloud", "jieba"}

try:
    for lib in libs:
        os.system("pip install"+lib)
        print("sucessfully installed")
except:
    print("Failed somehow")