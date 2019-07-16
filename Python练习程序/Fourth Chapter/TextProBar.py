# TextProBar.py

import time
scale = 50

print('执行开始'.center(scale//2, '-'))
Start = time.perf_counter()

for i in range(scale+1):
    a = i * '*'
    b = (scale-i)* '.'
    c = (i/scale)*100
    CurrT = time.perf_counter()-Start
    print('\r{:^3.0f}%[{}->{}]{:.2f}s'.format(c, a, b, CurrT), end="")
    time.sleep(0.1)
print('\n'+'执行结束'.center(scale//2, '-'))
