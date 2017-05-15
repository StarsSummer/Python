class Set():
    def __init__(self,aList):
	self.set=[]
	for x in aList: 
  	    self.addElement(x)
    def addElement(self,x):
        if not(self.isMember(x)):
            self.set.append(x)
    def deleteElement(self,x):
	i=0
        while i<len(self.set):
	    if x==self.set[i]:
		self.set.pop(i)
		break
	    i+=1  
    def union(self,Set2):
	Set3=self.set
	for x in Set2:
	    if not(self.isMember(x)):
		Set3.append(x)
	print Set3
    def substract(self,Set2):
	Set3=self.set
	for x in Set2:
	    i=0
	    while i<len(self.set):
	        if x==self.set[i]:
		    Set3.pop(i)
		    break
	        i+=1  
	print Set3
    def isMember(self,x):
	flag=0
	i=0
        while i<len(self.set):
	    if x==self.set[i]:
		flag=1
		break
	    i+=1
        return flag==1
    def printAll(self):
	print self.set

S=Set([1,2,3,1,2,5,6,7])
S.printAll()  
S.addElement(5)
S.addElement(4)
S.printAll()   
print S.isMember(3)
S.deleteElement(1)
S.printAll()
S.union([1,3,4,5])
S.substract([1,2,3,4,])
		
