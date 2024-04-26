import random

from colorama import Fore, Back, Style

def show():
    
    count = 1
    for row in play_ground:
        for column in row :
            if column != "_" : 
                if count in choices:
                    choices.remove(count)
                if column == "X":
                    print(Fore.RED,"X",end="")
                if column == "O":
                    print(Fore.BLUE,"O",end="")
            elif column == "_":
                print(Fore.BLACK,"_",end="")
            count += 1
        print()
    print()

def check_winner (winner,user , human , pc):
    cnt3 = 0 ; cnt4 = 0
    for row in range (0,3):
        cnt1 = 0 ; cnt2=0
        for col in range (0,3) :
            if col < 2 and play_ground[row][col] == play_ground[row][col+1] and play_ground[row][col] != "_" :   cnt1 += 1   
            if col < 2 and play_ground[col][row] == play_ground[col+1][row] and play_ground[row][col] != "_" :   cnt2 += 1 
            if col < 2 and row == 0 and  play_ground[col][col] == play_ground[col+1][col+1] and play_ground[col][col] != "_" :  cnt3 += 1
            if col<2 and  row == 2 and play_ground[row - col][col] == play_ground[row-col-1][col+1] and play_ground[row - col][col] != "_" :  cnt4 += 1
            if (cnt1 == 2) : 
                winner.append(play_ground[row][col]) 
                break
            if (cnt2 == 2) : 
                winner.append(play_ground[col][row])
                break
            if (cnt3 == 2) : 
                winner.append(play_ground[1][1]) 
                break
            if (cnt4 == 2) : 
                winner.append(play_ground[1][1])
                break
        if (cnt1 == 2 or cnt2 == 2 or cnt3 ==2 or cnt4 == 2):
            
            if winner[0] == pc or winner[0] == human:
                print("you lose")
            elif (winner[0] == user) :
                print (" you , win !!!")
            return True
            


    
play_ground=[["_","_","_"],
             ["_","_","_"],
             ["_","_","_"]]

choices=[1,2,3,4,5,6,7,8,9]
winner=[]
pc_human = input("you wanna play with pc or human : ")
user_input = input(" O  or  X  : ")
pc_input=""
human_input=""
winner=[]
gmae_counter = 0
while(1):
    #User /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    

    user_row = int(input("enter row : "))
    user_column = int(input("enter column : "))

    if  play_ground[user_row][user_column] == "_":
            play_ground[user_row][user_column]=user_input
    

    show()

    if(check_winner(winner,user_input,human_input,pc_input)):
        break
        
    
    #human /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    if pc_human == "human" :
        
        
        match user_input :
            case "X" :
                human_input = "O"
            case "O" :
                human_input = "X"

        human_row = int(input("enter row : "))
        human_column = int(input("enter column : "))

        if  play_ground[human_row][human_column] == "_":
            play_ground[human_row][human_column]=human_input
        

        show()
        if(check_winner(winner,user_input,human_input,pc_input)):
            break
    #PC/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    if pc_human == "pc" :
        

        
       
        match user_input :
            case "X" :
                pc_input = "O"
            case "O" :
                pc_input = "X"

        pc_row_column = random.choice(choices)
        count = 1
        flag = False
        for i in range (0,3):
            pc_row = i
            flag = False
            for j in range (0,3):
                pc_column = j
                if pc_row_column == count :
                    flag=True
                    break
                count += 1
            if flag :
                break
        play_ground[pc_row][pc_column]  =   pc_input

        show()
        
        if(check_winner(winner,user_input,human_input,pc_input)):
            break

    
    gmae_counter += 1
    
    if("_" not in play_ground[0] and "_" not in play_ground[1] and "_" not in play_ground[2] and gmae_counter > 4):
        print("no wins , no lose")
        break;