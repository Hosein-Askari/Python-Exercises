n=int(input("enter n : "))
x=0
for i in range (0,2*n):

    for j in range (0,2*n):
            if (j<=n+x and j>=n-x):
                  print("*",end="")
            else:
                  print(" ",end="")
    if (i<n-1):
        x += 1
    elif (i>=n-1):
        x -= 1              
    print("\n",end="")