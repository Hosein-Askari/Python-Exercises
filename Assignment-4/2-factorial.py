n = int(input())
fact = 1
for i in range (1,10):
    fact *= i 
    if fact ==n or fact > n:
        break
    
if fact == n :
        print ("Yes")
else:
        print("No")