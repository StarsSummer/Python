import random
sum=0
numa=list(range(101))
slice=random.sample(numa,20)
print("20个随机数生成方法一：",slice)
print("其中能被3整除的有： ",end='')
for x in range(19):
    if slice[x]%3==0:
        sum=sum+slice[x]
        print(slice[x],end='  ')
print('\n这些数字的和为:',sum) 

sum=0
numbb=[]
numb=list(range(101))
random.shuffle(numb)
print("20个随机数生成方法二：",end=' [')
for x in range(20):
    if numb[x]%3==0:
        numbb.append(numb[x])
        sum=sum+numb[x]
    print(numb[x],end='  ')
print(']')
print("其中能被3整除的有： ",numbb)
print('这些数字的和为:',sum) 

print("20个随机数生成方法三：",end=' ')
sum=0
numc=[]
numcc=[]
while len(set(numc))<20:
    numc.append(random.randint(0,100))
print(set(numc))
numcc=list(set(numc))
y=0
print("其中能被3整除的有： ",end='')
while y<len(numcc) :
    if numcc[y]%3==0:
        sum=sum+numcc[y]
        print(numcc[y],end='  ')
    y=y+1
print('\n这些数字的和为:',sum)
