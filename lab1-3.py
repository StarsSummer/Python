def rank(race):
    guess=0
    if (race[1]==2 and race[0]!=3)or(race[1]!=2 and race[0]==3):
        guess=guess+1
    if (race[1]==2 and race[4]!=4)or(race[1]!=2 and race[4]==4):
        guess=guess+1
    if (race[2]==1 and race[3]!=2)or(race[2]!=1 and race[3]==2):
        guess=guess+1
    if (race[2]==5 and race[3]!=3)or(race[2]!=5 and race[3]==3):
        guess=guess+1
    if (race[4]==4 and race[0]!=1)or(race[4]!=4 and race[0]==1):
        guess=guess+1
    if guess==5:
        return 1
    else:
        return 0
def perms(elements):
    if len(elements) <= 1:
        yield(elements)
    else:
        for perm in perms(elements[1:]):
            for i in range(len(elements)):
                yield(perm[:i] + elements[0:1] + perm[i:])
for item in list(perms([1, 2, 3, 4, 5])):
    if rank(item)==1:
        print(item)
