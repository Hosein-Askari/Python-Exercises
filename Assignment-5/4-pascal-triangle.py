n=int(input("enter n : "))
x=[]


for  i in range (0,n):
    
    x.append([])   
    for j in range(0,n):
        if(j<i and j != 0):
            x[i].append(x[i-1][j-1]+x[i-1][j])
            
        elif(i==j or j==0):
            x[i].append(1)
            
    print('   '.join(map(str,x[i])))

