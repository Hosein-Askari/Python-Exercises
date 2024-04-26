n=int(input("length of array"))
x=[]
for i in range(0,n):
    x.append(int(input()))
flag=False
for i in range(0,n):
    
    if   (i<n-1) and (x[i]>x[i+1])   :
        flag=True
        break
if flag :
    print("It isn't Sorted")
else:
    print("It's Sorted")