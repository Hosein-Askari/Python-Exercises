n=int(input("enter n : "))
m=int(input("enter m : "))


for  i in range (0,n):
    
        
    for j in range(0,m):
        if((i+1)*(j+1)>9):
            print((i+1)*(j+1),end="  ")
        else:
            print((i+1)*(j+1),end="   ")
    print("\n",end = "")