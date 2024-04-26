import random

n = int(input("enter n : "))

x=[]

while(n!=0):
    num=random.randint(0,n*n)
    if num not in x :
        x.append(num)
        n -= 1
    
print(x)