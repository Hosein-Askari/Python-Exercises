import os
import gtts
def read():

    if os.path.exists("Assignment-8/2-translate/database.txt"):
        f = open("Assignment-8/2-translate/database.txt","r")
    else:
        print ("can't read file, directory isn't valid.")
        exit(0)
    # for line in f:
    #     words.append(line)
    words = f.read().split("\n")  
    
    for i in range (0,len (words),2):
            dict={"en":words[i],"fa":words[i+1]}
            words_bank.append(dict)

    f.close

def write():
    f=f = open("Assignment-8/2-translate/database.txt","w")
    cnt = 0
    for word in words_bank:    
        for key,item in word.items():
            if(cnt>0):
                f.write("\n")
            f.write(item) 
            cnt += 1






def translate_english_to_persian():
    
    user_input = input("enter your sentences : ")

    

    user_sentences = " ".join(user_input.split('.'))

    user_words = user_sentences.split()

    str=""
    for word in user_words:
        for b_word in words_bank:
            if(word == b_word["en"]):
                str += b_word["fa"]+" "
                break
        else:
            str += " "
    print(str)
    voice = gtts.gTTS(str,lang = "en" ,slow=False)
    voice.save("Assignment-8/2-translate/voice.mp3")


def translate_persian_to_english():
    
    user_input = input("enter your sentences : ")

    

    user_sentences = " ".join(user_input.split('.'))

    user_words = user_sentences.split()

    str = ""
    for word in user_words:
        for b_word in words_bank:
            if(word == b_word["fa"]):
                str += b_word["en"]+" "
                break
        else:
            str += " "

    print(str)
    voice = gtts.gTTS(str,lang = "en" ,slow=False)
    voice.save("Assignment-8/2-translate/voice.mp3")        

def add_word():
    dict={}
    dict["en"]=input("enter your words in english ")
    dict["fa"]=input("enter your words in persian ")
    words_bank.append(dict)

   
words_bank=[] 
read()
#translate_english_to_persian()

print("welcome to translate")
while(1):
    print('''
    1- Translate english to persian
    2- Translate persian to english
    3- Add new words
    4- exit

    ''')

    n=int(input("what do  you wanna do? "))

    match n :
        case 1:
            translate_english_to_persian()
        case 2:
            translate_persian_to_english()
        case 3:
            add_word()
        case 4:
            write()
            break

