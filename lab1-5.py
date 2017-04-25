import random

def find(numa,numb):
    num=numa-numb
    nums=[int(num/1000),int(num%1000/100),int(num%100/10),num%10]
    print(nums)
    nums.sort()
    anum=nums[0]+10*nums[1]+100*nums[2]+1000*nums[3]
    bnum=nums[3]+10*nums[2]+100*nums[1]+1000*nums[0]
    if anum==numa:
        print(anum-bnum,'\n')
        return 
    else:
        find(anum,bnum)

for i in range(4):
    x=random.randint(1000,9999)
    find(x,0)

