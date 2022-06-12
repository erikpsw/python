#LIS最长上升子序列

a=[1,6,2,3,7,5]
n=len(a)-1
res=[1]#用于保存最长的序列长度
pos=[0]
#第一个为1
for i in range(1,n+1):
    print("i="+str(i))
    ma=0
    cur=0
    for j in range(i):
        print("j="+str(j))
        if a[n-j]>a[n-i]:
            if ma<res[j]:
                ma=res[j]
                cur=n-j
    pos.append(cur)
    res.append(ma+1)#状态转移方程，不要忘记加上1
res.reverse()
print(res)
pos.reverse()
print(pos)


i=res.index(max(res)) # 返回最大值的索引
print(a[i])
while(pos[i]!=0):
    i=pos[i]
    print(a[i])
#求出答案,不要想逆向，用reverse()反转更好想

