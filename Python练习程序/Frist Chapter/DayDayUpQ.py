#DayDayUpQ4.py
import time

Start = time.perf_counter()
def DayUP(df):
    DayUp = 1
    for i in range(365):
        if i % 7 in [0,6]:
            DayUp = DayUp * (1 - 0.01)
        else:
            DayUp = DayUp * (1 + df)
    return DayUp

df = 0.01
while DayUP(df) < 37.78:
    df += 0.001
print('工作日的努力参数是：{:.3f}'.format(df))
End = time.perf_counter()
print('程序运行时间：{0}ns'.format(End-Start))
