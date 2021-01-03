import math

while True:
    num=int(input())
    list = [2]
    for i in range(3, int(num)+3):
        yes = 1
        for j in list:
            if (i % j == 0):
                yes = 0
                break
        if (yes):
            list.append(i)
    temp=num
    ans=[]
    while(temp!=1):
        for j in list:
            if(temp%j==0):
                ans.append(j)
                temp=temp/j
                break
    print(ans)

