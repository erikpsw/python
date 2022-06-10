from fractions import Fraction

a1 =Fraction(1,2)
n=6
an=[]
an.append(a1)
t=Fraction(1,2)

for i in range(1,n):
    t=Fraction(t**2,t**2-t+1)
    an.append(t)

print(an)
bn=[]
bn.append(a1)
s=a1
for i in range(2,9):
    t=Fraction(6,i*(i-1)*(2*i-1)+12)
    bn.append(t)
    s=s+t

print(bn)
print(s)

