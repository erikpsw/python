import random
ori=[random.randint(0,50) for i in range(10)]
print(ori)
ok=1
while(ok):
    tot=0
    for i in range(len(ori)-1):
        if ori[i]>ori[i+1]:#不能取等，不然死循环
            temp=ori[i]
            ori[i]=ori[i + 1]
            ori[i + 1]=temp
            tot=tot+1
    if tot>0:
        ok=1
    else:
        ok=0
print(ori)

