
name = input("name : ")
lastname = input("last-name : ")

x = float(input("first-score "))
y = float(input("second-score "))
z = float(input("third-score "))
result = (x+y+z)/3

if (result>17 and result<=20):
    print("Great\n","Average-score = ",result )
elif(result>=12.5 and result<17):
    print("Normal\n","Average-score = ",result )
elif(result>=0 and result<12.5):
    print("Fail\n","Average-score = ",result )