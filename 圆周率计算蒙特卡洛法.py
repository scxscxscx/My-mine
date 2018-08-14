from random import random
from time import perf_counter
d=1000*1000
zhong=0.0
start=perf_counter()
for i in range(1,d):
    x,y=random(),random()
    zai=pow(x**2+y**2,0.5)
    if zai<=1.0:
        zhong+=1
pi=4*(zai/zhong)
print('圆周率值是：{}'.format(pi))
print('运行时间是：{:.5}s'.format(perf_counter()-start))
