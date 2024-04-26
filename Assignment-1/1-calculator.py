import math

op = 0
while(1):
    if (op != 12):
        print( '''
1. +
2. -
3. *
4. /
5.log
6.sqrt
7.sin
8.cos
9.tan
10.cot
11.factorial
12.exit''')
    
        op=int(input("\nenter what do you want to do ? (btw you should enter nummber) \n"))

    match op :
        case 12 :
            break
        case 1  :
            x=int(input("enter first number : "))
            y=int(input("enter second number : "))
            print ("result = " ,x+y)
            cnt=input("wanna continue ? (yes/no) ")
            if (cnt =="no"):
                op = 12
        case 2  :
            x=int(input("enter first number : "))
            y=int(input("enter second number : "))
            print ("result = " ,x-y)

            cnt=input("wanna continue ? (yes/no) ")
            if (cnt =="no"):
                op = 12
        case 3  :
            x=int(input("enter first number : "))
            y=int(input("enter second number : "))
            print ("result = " ,x*y)

            cnt=input("wanna continue ? (yes/no) ")
            if (cnt =="no"):
                op = 12
        case 4  :
            x=int(input("enter first number : "))
            y=int(input("enter second number : "))
            if(y>0):
                print ("result = ",x/y)
            else:
                print("can't divide by zero")

            cnt=input("wanna continue ? (yes/no) ")
            if (cnt =="no"):
                op = 12
        case 5  :
            x=int(input("enter number : "))
            print("result = ",math.log10(x))

            cnt=input("wanna continue ? (yes/no) ")
            if (cnt =="no"):
                op = 12
        case 6  :
            x=int(input("enter number : "))
            print("result = ",math.sqrt(x))
           
            cnt=input("wanna continue ? (yes/no) ")
            if (cnt =="no"):
                op = 12
        case 7  :
            x=int(input("enter degree : "))
            print("result = ",math.sin(x*math.pi/180))

            cnt=input("wanna continue ? (yes/no) ")
            if (cnt =="no"):
                op = 12
        case 8  :
            x=int(input("enter degree : "))
            print("result = ",math.cos(x*math.pi/180))

            cnt=input("wanna continue ? (yes/no) ")
            if (cnt =="no"):
                op = 12
        case 9  :
            x=int(input("enter degree : "))
            print("result = ",math.tan(x*math.pi/180))

            cnt=input("wanna continue ? (yes/no) ")
            if (cnt =="no"):
                op = 12
        case 10  :
            x=int(input("enter degree : "))
            print("result = ",1/math.tan(x*math.pi/180))
            cnt=input("wanna continue ? (yes/no) ")
            if (cnt =="no"):
                op = 12
        case 11  :
            x=int(input("enter number : "))
            print("result = ",math.factorial(x))
            cnt=input("wanna continue ? (yes/no) ")
            if (cnt =="no"):
                op = 12