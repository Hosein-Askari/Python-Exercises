import math
x = int (input("enter first number"))
y = int (input("enter second number"))
bmm = 0
if x>y :
    rep = x
    x  = y
    y = rep

for i in range (y,x*y+1,y):
        if i % x == 0 :
            print("kmm : ", i)
            break
            