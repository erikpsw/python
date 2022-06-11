import random
a=[random.randint(0,50) for i in range(10)]
print(a)

def merge(f,b):
    print("f="+str(f)+"，b="+str(b))
    if b-f>1:
        mid=int(f+(b-f)/2)
        print(mid)
        merge(f,mid)
        merge(mid+1, b)
        p=f
        q=mid+1
        tem=[]
        while(p<=mid or q<=b):
            print("p=" + str(p) + "，q=" + str(q))
            if p<=mid and q<=b:
                if a[p]<a[q]:
                    tem.append(a[p])
                    p=p+1
                else:
                    tem.append(a[q])
                    q = q + 1
            elif p>mid:
                for i in range(q,b+1):
                    tem.append(a[i])
                break
            else:
                for i in range(p,mid+1):
                    tem.append(a[i])
                break
        print("temp=")
        print(tem)
        t=0
        for i in range(f,b+1):
            a[i]=tem[t]
            t=t+1
    if b-f==1:
        if a[f]>a[b]:
            a[f] , a[b]=a[b] , a[f]

merge(0,len(a)-1)
print(a)

#总结，range(a,b)=[a,b)
#注意下标，改正从0开始，len就是个数

