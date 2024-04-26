import random

rand_number = random.randint(10,40)
count = 0
while(1):
    guessing_number=int(input())
    count += 1
    if (rand_number == guessing_number):
        print("Great, you guess right")
        break;
    elif(rand_number>guessing_number):
        print("Not correct, try greater numbers")
    elif(rand_number<guessing_number):
        print("Not correct, try lower numbers")

print("Tries : ",count)