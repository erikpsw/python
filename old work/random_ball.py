import random

count=0
ok=0

for i in range(10000):
    count+=1
    result=random.sample(range(1,11),3)
    print(result)
    if(1 in result) or (2 in result) or (3 in result):
        ok+=1
        print("yes")
    else:
        print("no")

print(ok/count)
