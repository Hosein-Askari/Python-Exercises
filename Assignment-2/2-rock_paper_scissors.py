import random

user_score = 0
computer_score = 0
computer_choice = ""
while(1):
    x = random.randint(1,3)
    
    match x :
        case 1:
            computer_choice = "rock"
        case 2:
            computer_choice = "paper"
        case 3:
            computer_choice = "scissors"

    user_choice = input("\n enter your choice : ")

    if (user_choice == "rock" and  computer_choice == "scissors") :
        user_score += 1
    elif (user_choice == "rock" and computer_choice == "paper") :
        computer_score += 1
    elif (user_choice == "scissors" and computer_choice == "paper") :
        user_score += 1
    elif (user_choice == "scissors" and computer_choice == "rock" ) :
        computer_score += 1
    elif (user_choice == "paper"  and  computer_choice == "rock") :
        user_score += 1
    elif (user_choice == "paper" and computer_choice == "scissors") :
        computer_score += 1
    
    
    print("👤",user_score)
    print("💻",computer_score)

    if(user_score == 3 ):
        print("You win!")
        break

    elif(computer_score == 3):
        print("You lose")
        break
    