x=input("enter first  side : ")
y=input("enter second side : ")
z=input("enter third  side : ")

if (x+y > z and x+z > y and y+z > x):
    print("yes")
else:
    print("no")