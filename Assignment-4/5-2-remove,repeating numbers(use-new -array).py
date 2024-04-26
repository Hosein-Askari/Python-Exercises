n=int(input("enter length of array : "))
x=[]
new_x=[]
falg =False
for i in range (0,n):
    x.append(int(input()))


for i in range (0,len(x)):
    flag = False
    for j in range (0,len(new_x)):
        if x[i] == new_x[j] :
            flag=True
            break
    if(flag == False):
        new_x.append(x[i])

print(new_x)