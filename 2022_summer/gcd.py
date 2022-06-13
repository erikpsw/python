import numpy as np

def gcd(a,b):
    if a<b:
        a,b=b,a
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

print("gcd={}".format(str(gcd(1573,1859))))
#内层函数没有返回值，需要返回递归解

def gcd_prime(*num):
    a=list(num)
    while(len(a)>=3):
        a.append(gcd(a[0],a[1]))
        del a[0],a[1]
    return gcd(a[0],a[1])

print("gcd={}".format(str(gcd_prime(216,64,1000))))

#gcd(a,b)=ma+nb，不用递归(动态规划),请让a>b
def extebded_euclid(a,b):
    arr=np.array([[1,0],[0,1]])
    i=0
    while(a%b!=0):
        q=(a-a%b)/b
        arr = np.append(arr, np.array([arr[i] - q * arr[i + 1]]), axis=0)
        i=i+1
        a,b=b,a%b
    print("m={},n={}".format(int(arr[-1][0]),int(arr[-1][1])))
extebded_euclid(83,36)#from课本
extebded_euclid(99,78)#from算法导论P549



