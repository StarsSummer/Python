import random

point=0
x=-5
while x<=5:
    for i in range(10):
        y=random.uniform(-4,4)
        if(x*x/25+y*y/16<1):
            point=point+1
    x=x+1
s=point/100*80
print('取100个点下，椭圆面积的近似值为：',s)

point=0
x=-5
while x<=5:
    for i in range(100):
        y=random.uniform(-4,4)
        if(x*x/25+y*y/16<1):
            point=point+1
    x=x+0.1
s=point/10000*80
print('取10000个点下，椭圆面积的近似值为：',s)

point=0
x=-5
while x<=5:
    for i in range(1000):
        y=random.uniform(-4,4)
        if(x*x/25+y*y/16<1):
            point=point+1
    x=x+0.01
s=point/1000000*80
print('取1000000个点下，椭圆面积的近似值为：',s)
