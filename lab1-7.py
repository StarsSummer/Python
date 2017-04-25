import random

price=input('请输入红包总额:')
bags=list(range(1,int(price)-1))
people=input('请输入派发的人数:')
money=random.sample(bags,int(people)-1)
money.sort()
money.append(int(price))
money.insert(0,0)
for x in range(int(people)):
    money[x]=money[x+1]-money[x]
money.pop()
print("20个随机数生成方法一：",money)


