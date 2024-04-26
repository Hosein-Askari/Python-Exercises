import math
x = int (input("enter first number"))
y = int (input("enter second number"))
bmm = 0
if x>y :
    rep = x
    x  = y
    y = rep

for i in range (1,x+1):
        if (x%i == 0) and (y % i == 0) :
            if i > bmm:
                 bmm = i

print("bmm : ", bmm)
            