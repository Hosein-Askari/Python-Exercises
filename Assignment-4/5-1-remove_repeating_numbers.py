n=int(input("enter length of array : "))
x=[]
flag = False
for i in range (0,n):
    x.append(int(input()))

i=0
j=0
while (1):
    
    
    j= i+1
    
    while (1):
        
        if x[i] == x[j] :            
            x.remove(x[j])
            i=i-1
            break
        
        j += 1
        if (j==len(x)):
            break
    i += 1        
    if(i==len (x)-1):
        break
print(x)