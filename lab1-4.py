import time
alist=[]
blist=[]
print('list是一个可变的有序表，所以，append可以往list中追加元素到末尾,insert可以把元素插入到指定的位置')
t0=time.time()
for x in range(50000):
    alist.append(50001-x)
print('append use time:',time.time()-t0)
t1=time.time()
for x in range(50000):
    blist.insert(x,50001-x)
print('insert use time:',time.time()-t1)


    
