n=8#棋盘大小
c=l=0
ok=[[0 for i in range(3)] for j in range(2*n)]#用于判断位置
res=[]
sol=[0 for i in range(n)]

def search(i):#层数
    if i==n:#要用完第七层，不能n-1
        res.append(ok)
        print(sol)
    else:
        for j in range(n):
            if ok[j-i+n][0]==0 and ok[i+j][1]==0 and ok[j][2]==0:
                ok[j-i+n][0]=1
                ok[i +j][1]=1
                ok[j][2]=1
                sol[i]=j
                search(i+1)
                ok[j-i+n][0] = 0
                ok[i +j][1] =0
                ok[j][2] = 0

search(0)
print(len(res))

