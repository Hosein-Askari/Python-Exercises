import random
bank_words  = ["apple" , "bmw" , "book" , "shoes" , "boy" , "lincoln"]

x = random.randint(0,len(bank_words)-1)
word = bank_words[x]
guess_chars = []
count =0


for i in range(0,len (word)+1):
    end_flag = False
    for j in range (0,len (word)):
        if word[j] in guess_chars:
            print(word[j],end=" ")
        else:
            print("_",end=" ")
            end_flag=True
    if (end_flag==False):
         break
    if i <len(word):
        user_choice=input("\ninput charcter : ")
        flag=False
        for j in range (0,len (word)):
            if (user_choice == word[j] ):
                guess_chars.append(user_choice)
                flag = True
                break;
        if (flag==False):
                print("psych you have wrong guess")    

        
