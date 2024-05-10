#!pip install pytelegrambotapi
import telebot
from telebot import types
import random
#!pip install jdatetime
import jdatetime
#!pip install gtts
import gtts
#!pip install qrcode
import qrcode


state=""
x=0
my_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
btn1 = types.KeyboardButton("New game")
my_keyboard.add(btn1)

bot=telebot.TeleBot("6995312797:AAHwVoAUhTNrl0zaL8A90Eu0LE93lTSEEmE",parse_mode=None)

@bot.message_handler(commands=['start'])
def welcom(messege):
    name = bot.get_chat(messege.chat.id).first_name
    name = "welcome "+str(name)
    bot.send_message(messege.chat.id,name,reply_markup=types.ReplyKeyboardRemove())

@bot.message_handler(commands=['game'])
def game(messege):
    global x 
    x= random.randint(0,100)
    bot.reply_to(messege,"gusse number")
    global state
    state="game"

@bot.message_handler(commands=['age'])
def age(messege):
    bot.reply_to(messege,"enter your age in year/month/day form",reply_markup=types.ReplyKeyboardRemove())
    global state
    state="age"
    
@bot.message_handler(commands=['voice'])
def voice(messege):
    bot.reply_to(messege,"enter your sentences ",reply_markup=types.ReplyKeyboardRemove())
    global state
    state="voice"

@bot.message_handler(commands=['max'])
def max(messege):
    bot.reply_to(messege,"enter your numbers with comma(,) : ",reply_markup=types.ReplyKeyboardRemove())
    global state
    state="max"

@bot.message_handler(commands=['argmax'])
def argmaax(messege):
    bot.reply_to(messege,"enter your numbers with comma(,) : ",reply_markup=types.ReplyKeyboardRemove())
    global state
    state="argmax"

@bot.message_handler(commands=['qrcode'])
def qrrcode(messege):
    bot.reply_to(messege,"enter your sentences : ",reply_markup=types.ReplyKeyboardRemove())
    global state
    state="qrcode"

@bot.message_handler(commands=['help'])
def qrrcode(messege):
    bot.reply_to(messege,'''/game : It's about guessing numbers 
    /age : give us your date of birth and we tell how old you are
    /voice : enter your sentences and you will get voice 
    /max  : enter your numbers , you will get max number
    /argmax : enter your numbers , this time you will get  index of max number
    /qrcode : enter your sentences and get qrcode ''',reply_markup=types.ReplyKeyboardRemove())
    
    global state
    state="help"



@bot.message_handler(func=lambda m:True)
def echo_all(messege):   
    
    if state == "game":
        if messege.text == "New game":
            global x 
            x= random.randint(0,100)
            bot.reply_to(messege,"gusse number")
            
        else :
            if (x> int(messege.text)):
                bot.send_message(messege.chat.id,"guess higher",reply_markup=my_keyboard)
            elif(x< int(messege.text)):
                bot.send_message(messege.chat.id,"guess lower",reply_markup=my_keyboard)
            elif(x== int(messege.text)):
                bot.send_message(messege.chat.id,"Congratulations!!",reply_markup=my_keyboard)
            
    elif state == "age":
        year = (messege.text).split('/')
        yearj = str(jdatetime.date.today()).split('-')
        
        if(int(year[2])>int(yearj[2])):
            if int(year[1])>6:
                year[2]=str(int(yearj[2])+30 - int(year[2]))
                yearj[1]=str(int(yearj[1])-1)
                
            elif int(year[1])<7:
                year[2]=str(int(yearj[2])+31 - int(year[2]))
                yearj[1]=str(int(yearj[1])-1)
                
        else:
                year[2]=str(int(yearj[2]) - int(year[2]))
        if(int(year[1])>int(yearj[1])):
                year[1]=str(int(yearj[1])+12 - int(year[1]))
                yearj[0]=str(int(yearj[0])-1)               
        else:
            year[1]=str(int(yearj[1]) - int(year[1]))

        year[0]=str(int(yearj[0])-int(year[0]))
        bot.send_message(messege.chat.id,year[0]+"years "+year[1]+"months "+year[2]+"days")

    elif state == "voice": 
        strr = messege.text
        voice = gtts.gTTS(strr,lang = "en" ,slow=False)
        voice.save("voice.mp3")
        voice = open("voice.mp3", 'rb')
        bot.send_voice(messege.chat.id,voice)

    elif state == "max":
        max = 0
        numbers = (messege.text).split(',')
        for i in range(0,len(numbers)):
            if int(numbers[i])>max:
                max= int(numbers[i])
        bot.send_message(messege.chat.id,"Max : "+str(max))
    
    elif state == "argmax":
        max = 0
        maxi = 0
        numbers = messege.text.split(',')
        for i in range(0,len(numbers)):
            if int(numbers[i])>max:
                max= int(numbers[i])
                maxi = i
        bot.send_message(messege.chat.id,"ArgMax : "+str(maxi+1))

    elif state == "qrcode":
        code= qrcode.make(messege.text)
        code.save("qrcode.png")
        photo = open('qrcode.png', 'rb')
        bot.send_photo(messege.chat.id, photo)

   
        
bot.infinity_polling()