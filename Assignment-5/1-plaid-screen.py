n=int(input("enter n : "))
m=int(input("enter m : "))


for  i in range (0,n):
    
        
    for j in range(0,m):
        if(i%2==0):
            if (j % 2) == 0:
                print("*",end="")
            else:
                print("#",end="")
        else:
            if (j % 2) == 0:
                print("#",end="")
            else:
                print("*",end="")
    print("\n",end = "")