list=[2]
print(2)
for i in range(3,100):
    yes=1
    for j in list:
        if(i%j==0):
            yes=0
            break
    if(yes):
        list.append(i)
        print(i)
#fuck,我再也不用c++了，就这？？？浪费我宝贵的时间