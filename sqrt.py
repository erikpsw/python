import math
def lim(i):
    A=math.sqrt(i+1)
    while i>2:
        i=i-1
        A=math.sqrt(1+i*A)
    return A
print(lim(1000))
