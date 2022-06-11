import random
a=[random.randint(0,50) for i in range(10)]
print(a)

def qsort(f,b):
    print("f="+str(f)+"，b="+str(b))
    if (b-f)>=2:
        j=f#最终的位置
        m=a[b-1]#中间变量
        for i in range(f,b):
            if a[i]<=m:
                a[j],a[i]=a[i],a[j]
                j=j+1
        print(a)
        qsort(f,j-1)
        qsort(j,b)
#最后分为(f,j-1),(j,b)

qsort(0,len(a))
print(a)