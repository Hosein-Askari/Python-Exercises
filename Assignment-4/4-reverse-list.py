
n=int(input("enter length of array : "))
x=[]
 
for i in range (0,n):
    x.append(int(input()))

count = 0 
temp= 0
for i in range (0,len(x)) :
    if( (i+count)<(len(x)-1-count) )and ( (i+count) != (len(x)-1-count) ) :
        temp = x[i+count]
        x[i+count]=x[len(x)-1-count]
        x[len(x)-1-count]=temp
    else:
        break
    count += 1

print(x)