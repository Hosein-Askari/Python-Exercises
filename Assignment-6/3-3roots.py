import math
import cmath
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c = "))
d=int(input("d = "))

Δ=(18*a*b*c*d)  -  (4*(pow(b,3)*d)) + (b**2*c**2) - (4*a*pow(c,3)) - (27*a**2 * d**2)
Δ0=b**2 - 3*a*c
Δ1=2*pow(b,3)-9*a*b*c+27*a**2*d
Δ2=-1*(27*a**2*d)

C=math.cbrt((Δ1+math.sqrt(Δ2))/2)

u1 = 1
u2 =complex(-1/2,math.sqrt(3)/2)
u3 = complex(-1/2,-1*math.sqrt(3)/2)
if(Δ>0):
    x1= -1/3*a*(b+C+Δ0/C)
    x2= -1/3*a*(b+u2*C+Δ0/C)
    x3= -1/3*a*(b+u3*C+Δ0/C)
    print(x1,x2,x3)
elif (Δ==0):
    x1= -1/3*a*(b+C+Δ0/C)
    print(x1)
elif (Δ<0):
    x1= -1/3*a*(b+C+Δ0/C)
    print(x1,u1,u2)