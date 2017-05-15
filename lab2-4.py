def BubbleSort(aList):
    count=1
    while count!=0:
	count=0
	for x in range(len(aList)-1):
	    if aList[x]>aList[x+1]:
		aList[x],aList[x+1]=aList[x+1],aList[x]
                count+=1
    print aList
def QuickSort(aList):
    Quick(aList,0,len(aList)-1)
    print aList
def Quick(L,low,high):
    if low<high:
	split=partition(L,low,high)
	Quick(L,low,split-1)
        Quick(L,split+1,high)
def partition(L,low,high):
    pivot=L[low]
    left=low+1
    right=high
    while True:
	while L[left]<=pivot:
	    if left==right:
		break
 	    left+=1
	while L[right]>pivot:
	    right-=1
	if left<right:
	    L[left],L[right]=L[right],L[left]
	else:
	    break
    L[low],L[right]=L[right],L[low]
    return right
BubbleSort([2,5,1,12,20,16,7,6])
QuickSort([2,5,1,12,20,16,7,6])
