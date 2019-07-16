# -*- coding: UTF-8 -*-
"""

author:wu
time:2019/6/24 21:16

"""

try:
    f = open("exist.txt", 'w')
    sum1 = 1 + '1'
    f = open("my_list.txt")
    print(f.read)
    f.close()
except OSError as reason:
    print("文件出错的原因是:{0}".format(str(reason)))
except TypeError as reason:
    print("类型出错的原因是:{0}".format(reason))
except FileExistsError as reason:
    print("出错了T_T！！")
finally:
    f.close()
