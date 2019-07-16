# -*- coding: UTF-8 -*-
"""
author:wu
time:2019/7/2 21:23
"""
import jieba
import wordcloud
from matplotlib.image import imread

f = open('关于实施乡村振兴战略的意见.txt', 'r', encoding= 'utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)

c = wordcloud.WordCloud(font_path="msyh.ttc",
                        width=1000, height=700, background_color='white',
                        max_words=15)
c.generate(txt)
c.to_file('乡村振兴.png')

