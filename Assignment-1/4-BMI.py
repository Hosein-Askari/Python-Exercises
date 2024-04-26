w = float(input("enter weight in kg : "))
h = float(input("height in m : "))

bmi = w/(h*h)

if (bmi <18.5 ):
    print(bmi ," UnderWeight")
elif(bmi>=18.5 and bmi <25):
    print(bmi," NormalWeight")
elif(bmi>=25 and bmi <30):
    print(bmi," OverWeight")
elif(bmi>=30 and bmi <35):
    print(bmi," Obesity")
elif(bmi>=35 and bmi <40):
    print(bmi," Extreme Obesity")