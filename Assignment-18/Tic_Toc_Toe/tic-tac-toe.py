import random
import datetime
from functools import partial
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication,QGraphicsDropShadowEffect,QMessageBox
from PySide6.QtGui import QIcon,QColor,QPixmap,QPainter
from PySide6.QtCore import QSize,QTimer,Qt



player = 1
set = 0
X_win=0
O_win=0
choices=[1,2,3,4,5,6,7,8,9]
end_set=False
mode=""


def Mode():
    global mode
    new_game()   
    for i in range(0, 3):
        for j in range(0, 3):
            try:
                buttons[i][j].clicked.disconnect()
            except TypeError:
                pass  # اگر قبلاً رویدادی متصل نبوده، نادیده بگیر
    
    if window.radioButton.isChecked():
        mode="player"
        for i in range(0,3):
            for j in range (0,3):
                buttons[i][j].clicked.connect(partial(set_choice,i,j,mode))
    elif window.radioButton_2.isChecked():
        mode="pc"
        for i in range(0,3):
            for j in range (0,3):
                buttons[i][j].clicked.connect(partial(set_choice,i,j,mode))



def set_choice(x,y,mode):
    global player
    global first_time
    
    if mode=="player":
        if   buttons[x][y].text()=="":

            if player == 1:
                current_stylesheet = buttons[x][y].styleSheet()
                new_stylesheet = current_stylesheet + "font-size: 5px; color: rgba(0, 0, 0, 0);"
                
                buttons[x][y].setText("o")  
                buttons[x][y].setStyleSheet(new_stylesheet)
                buttons[x][y].setIcon(QIcon('Assignment-18/Tic_Toc_Toe/O.png'))
                buttons[x][y].setIconSize(QSize(150,150))
                player = 2

            elif player==2:
                


                current_stylesheet = buttons[x][y].styleSheet()
                new_stylesheet = current_stylesheet + "font-size: 5px; color: rgba(0, 0, 0, 0);"
                buttons[x][y].setText("x")  
                buttons[x][y].setStyleSheet(new_stylesheet)
                buttons[x][y].setIcon(QIcon('Assignment-18/Tic_Toc_Toe/X.png'))
                buttons[x][y].setIconSize(QSize(149,149))
                player = 1

    elif mode == "pc":


        if player == 1 and   buttons[x][y].text()=="":
            current_stylesheet = buttons[x][y].styleSheet()


            new_stylesheet = current_stylesheet + "font-size: 5px; color: rgba(0, 0, 0, 0);"


            
            buttons[x][y].setText("o")  
            buttons[x][y].setStyleSheet(new_stylesheet)
            buttons[x][y].setIcon(QIcon('Assignment-18/Tic_Toc_Toe/O.png'))
            buttons[x][y].setIconSize(QSize(150,150))
            player = 2
            choice=x*2+y+x+1
            index=choices.index(choice)
            choices.pop(index)
        if player==2:
            QTimer.singleShot(700,lambda:select_pc_choice())



def select_pc_choice():
            global player

            if len(choices) >1:
                choice = random.choice(choices)
   
                x=0
                y=0
                for i in range (0,3):
                    for j in range(0,3):
                        if choice == (i*2+j+i+1):

                            x=i
                            y=j
                index=choices.index(choice)
                choices.pop(index)


                current_stylesheet = buttons[x][y].styleSheet()
                new_stylesheet = current_stylesheet + "font-size: 5px; color: rgba(0, 0, 0, 0);"
                buttons[x][y].setText("x")  
                buttons[x][y].setStyleSheet(new_stylesheet)
                buttons[x][y].setIcon(QIcon('Assignment-18/Tic_Toc_Toe/X.png'))
                buttons[x][y].setIconSize(QSize(149,149))
                player = 1



 








def check():
    global X_win,O_win,set,end_set,mode
    win_flag = False
    
    for i in range (3):
            j=0         
            
            if   buttons[i][j].text() == buttons[i][j+1].text()== buttons[i][j+2].text() and buttons[i][j].text() != "":
                win(buttons[i][j],buttons[i][j].iconSize().width(),[[i,j],[i,j+1],[i,j+2]])
                win_flag=True
                break
            if   buttons[j][i].text() == buttons[j+1][i].text()== buttons[j+2][i].text() and buttons[j][i].text() != "":
                win(buttons[j][i] ,buttons[j][i].iconSize().width(),[[j,i],[j+1,i],[j+2,i]])
                win_flag=True
                break
            if buttons[j][j].text() == buttons[j+1][j+1].text()== buttons[j+2][j+2].text() and buttons[j+1][j+1].text() != "":
                win(buttons[j][j] ,buttons[j][j].iconSize().width(),[[j,j],[j+1,j+1],[j+2,j+2]])
                win_flag=True
                break
            if buttons[j+1][j+1].text() == buttons[j][j+2].text()== buttons[j+2][j].text() and buttons[j+1][j+1].text() != "":   
                win(buttons[j+1][j+1] ,buttons[j+1][j+1].iconSize().width(),[[j+1,j+1],[j,j+2],[j+2,j]])
                win_flag=True
                break
 

    full_flag=True
    if not win_flag:
        for i in range (3):
            for j in range(3):
                if buttons[i][j].text() == "":
                    full_flag=False
                    break
        if  full_flag:
                end_set=True
                QTimer.singleShot(800,lambda:reset_game())
                
       



        if window.radioButton.isChecked() or window.radioButton_2.isChecked():

            if player == 1:


                

                stylesheet_1 =  """ background-color: rgba(255, 255, 255,25);
                    border-radius : 25px solid black;
                    color: white;
                    background-image: url('Assignment-18/Tic_Toc_Toe/xx.png');
                    background-repeat: no-repeat;
                    background-position: left;
                    padding: 0 40px"""
                stylesheet_2 =   """ background-color: rgb(16, 139, 255);
                                    border-radius : 25px solid black;
                                    color: white;
                                    background-image: url('Assignment-18/Tic_Toc_Toe/oo.png');
                                    background-repeat: no-repeat;
                                    background-position: left;
                                    padding: 0 40px"""
                window.lineEdit.setStyleSheet(stylesheet_2)
                window.lineEdit_3.setStyleSheet(stylesheet_1)
            elif player==2:
                stylesheet_1 =  """ background-color: rgba(255, 255, 255,25);
                                    border-radius : 25px solid black;
                                    color: white;
                                    background-image: url('Assignment-18/Tic_Toc_Toe/oo.png');
                                    background-repeat: no-repeat;
                                    background-position: left;
                                    padding: 0 40px"""
                stylesheet_2 =   """ background-color: rgb(253, 15, 190);
                                    border-radius : 25px solid black;
                                    color: white;
                                    background-image: url('Assignment-18/Tic_Toc_Toe/xx.png');
                                    background-repeat: no-repeat;
                                    background-position: left;
                                    padding: 0 40px"""
                window.lineEdit.setStyleSheet(stylesheet_1)
                window.lineEdit_3.setStyleSheet(stylesheet_2)  
        else:
                mode=""
                Mode()
                stylesheet_1 =  """ background-color: rgba(255, 255, 255,25);
                                    border-radius : 25px solid black;
                                    color: white;
                                    background-image: url('Assignment-18/Tic_Toc_Toe/oo.png');
                                    background-repeat: no-repeat;
                                    background-position: left;
                                    padding: 0 40px"""
                window.lineEdit.setStyleSheet(stylesheet_1)
                stylesheet_2 =  """ background-color: rgba(255, 255, 255,25);
                    border-radius : 25px solid black;
                    color: white;
                    background-image: url('Assignment-18/Tic_Toc_Toe/xx.png');
                    background-repeat: no-repeat;
                    background-position: left;
                    padding: 0 40px"""               
                
                window.lineEdit_3.setStyleSheet(stylesheet_2)


    window.lineEdit.setText(f"{O_win}")
    window.lineEdit_3.setText(f"{X_win}")
    window.lineEdit_2.setText(f"set : {set}") 



timer2 = None
timer2_count=0
def win(icon,size,points):
    global X_win,O_win,timer2,end_set,timer2_count
    
    if timer2 is None:
        timer2=QTimer()
        timer2.timeout.connect(partial(toggle_opacity,icon.icon(),size,points))
        timer2.start(400)
    else:
        timer2.start(400)


    if not end_set: 
            if icon.text()=="o":
                O_win += 1
                stylesheet_1 =  """ background-color: rgba(255, 255, 255,25);
                border-radius : 25px solid black;
                color: white;
                background-image: url('Assignment-18/Tic_Toc_Toe/xx.png');
                background-repeat: no-repeat;
                background-position: left;
                padding: 0 40px"""
                stylesheet_2 =   """ background-color: rgb(16, 139, 255);
                                border-radius : 25px solid black;
                                color: white;
                                background-image: url('Assignment-18/Tic_Toc_Toe/oo.png');
                                background-repeat: no-repeat;
                                background-position: left;
                                padding: 0 40px"""
                window.lineEdit.setStyleSheet(stylesheet_2)
                window.lineEdit_3.setStyleSheet(stylesheet_1)
            elif icon.text()=="x":
                X_win += 1
                stylesheet_1 =  """ background-color: rgba(255, 255, 255,25);
                                border-radius : 25px solid black;
                                color: white;
                                background-image: url('Assignment-18/Tic_Toc_Toe/oo.png');
                                background-repeat: no-repeat;
                                background-position: left;
                                padding: 0 40px"""
                stylesheet_2 =   """ background-color: rgb(253, 15, 190);
                                border-radius : 25px solid black;
                                color: white;
                                background-image: url('Assignment-18/Tic_Toc_Toe/xx.png');
                                background-repeat: no-repeat;
                                background-position: left;
                                padding: 0 40px"""
                window.lineEdit.setStyleSheet(stylesheet_1)
                window.lineEdit_3.setStyleSheet(stylesheet_2)  
            end_set=True

    
    if  timer2.isActive():
        
        timer2_count += 1  
      
        if (timer2_count)>7:
            reset_game()
            timer2_count=0

def new_game():
    global timer2,player,end_set,X_win,O_win,set
    player=1
    X_win=0
    O_win=0
    set=0
    end_set=False



    for i in range(0,3):
        for j in range (0,3):
            buttons[i][j].setIcon(QIcon())
            buttons[i][j].setText("")
    
    if timer2 is not  None :         
        timer2.stop()
        timer2=None  #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!اینجا اگر متغیر تایمر دومی رو از بین نبری همون ایکون قبلی اجرا میشه چون شی تایمر قبلی فقط 
    
    choices.clear()
    for i in range(1,10):                                                                            #            شده ولی از بین نرفتهstopش
        choices.append(i)

   
    window.radioButton.setCheckable(True) 
    window.radioButton_2.setCheckable(True)



def reset_radio_button():
    window.radioButton.setCheckable(False) 
    window.radioButton_2.setCheckable(False) 
    window.radioButton.setStyleSheet("""QRadioButton {
color:                  white;
background-color:  rgba(0,0,0,0);
}


QRadioButton::indicator {
    width:                  10px;
    height:                 10px;
    border-radius:          7px;

}


QRadioButton::indicator:checked {
    background-color:       qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(5, 57, 226), stop:0.6 rgb(156, 7, 106));

    border:                 2px solid white;
}

QRadioButton::indicator:unchecked {
    background-color:       white;
    border:                2px solid white;
}""")



def reset_game():
    global timer2,player,end_set,set
    player=1

    if timer2 is not  None :  
               
        timer2.stop()
        timer2=None
    if end_set:
        set += 1
        end_set=False
    
    for i in range(0,3):
        for j in range (0,3):
            buttons[i][j].setIcon(QIcon())
            buttons[i][j].setText("")
    
    
    choices.clear()
    for i in range(1,10):                                                                            
        choices.append(i)



def About_button():
    msg=QMessageBox(text="""It's Tic Tac Toe Game, enjoy it.
The goal of the game is to be the first player to get three of your marks in a row (horizontally, vertically, or diagonally).""")
    msg.exec()

def update_icon_sizes():

        for i in range(3):
            for j in range(3):
                button = buttons[i][j]
                # icon_size=button.iconSize().width()
                button_size = button.size()
                # if(icon_size==button_0_size):
                new_icon_size = min(button_size.width(), button_size.height()) - 20  # کاهش اندازه برای حاشیه
                button.setIconSize(QSize(new_icon_size, new_icon_size))
                


            
def set_icon_opacity(icon,size, opacity):
    # icon = QIcon(icon_path)
    # icon=QIcon('Assignment-18/Tic_Toc_Toe/copy8.png')
    pixmap = icon.pixmap(size,size)   
    if pixmap.isNull():
        print("Failed to load the icon")
        return QIcon()  

    
    transparent_pixmap = QPixmap(pixmap.size())
    transparent_pixmap.fill(Qt.transparent)

    painter = QPainter(transparent_pixmap)
    painter.setOpacity(opacity)  # تنظیم شفافیت
    painter.drawPixmap(0, 0, pixmap)
    painter.end()

    return QIcon(transparent_pixmap)

visible = [True]
# تابع تغییر شفافیت به صورت ناگهانی
def toggle_opacity(icon,size,points):

    if visible[0]:
        icon_with_opacity = set_icon_opacity(icon,size, 0)  # تنظیم شفافیت به 0%
        buttons[points[0][0]][points[0][1]].setIcon(icon_with_opacity)
        buttons[points[1][0]][points[1][1]].setIcon(icon_with_opacity)
        buttons[points[2][0]][points[2][1]].setIcon(icon_with_opacity)
        visible[0] = not visible[0]


    else:
        icon_with_opacity = set_icon_opacity(icon,size, 1)  # تنظیم شفافیت به 100%
        buttons[points[0][0]][points[0][1]].setIcon(icon_with_opacity)
        buttons[points[1][0]][points[1][1]].setIcon(icon_with_opacity)
        buttons[points[2][0]][points[2][1]].setIcon(icon_with_opacity)
        
        visible[0] = not visible[0]
    
            
        












loader = QUiLoader()
app = QApplication([])

window = loader.load('Assignment-18/Tic_Toc_Toe/tic_toc_toe.ui')

timer3=QTimer()
timer3.timeout.connect(update_icon_sizes)
timer3.start(1)



timer1= QTimer()
timer1.timeout.connect(check)
timer1.start(500)



window.show()


sample=[]
for i in range(0,9):
    sample.append(f"shadow_{i}")

    sample[i]=QGraphicsDropShadowEffect()
   
    sample[i].setBlurRadius(50) 
    sample[i].setColor(QColor(47, 255, 255, 255))
    sample[i].setOffset(0,0)

    button =f"pushButton_{i+1}"

    getattr(window,button).setGraphicsEffect(sample[i])


window.pushButton.released.connect(lambda:new_game())
window.pushButton.pressed.connect(lambda:reset_radio_button())
window.pushButton_10.clicked.connect(lambda:About_button())
# window.pushButton.released.connect(partial(win))
buttons=[[window.pushButton_1,window.pushButton_2,window.pushButton_3],
         [window.pushButton_4,window.pushButton_5,window.pushButton_6],
         [window.pushButton_7,window.pushButton_8,window.pushButton_9]]

window.lineEdit.setContextMenuPolicy(Qt.NoContextMenu)
window.lineEdit_2.setContextMenuPolicy(Qt.NoContextMenu)
window.lineEdit_3.setContextMenuPolicy(Qt.NoContextMenu)
window.lineEdit.setAlignment(Qt.AlignRight)
window.lineEdit_2.setAlignment(Qt.AlignCenter)
window.lineEdit_3.setAlignment(Qt.AlignRight)


window.radioButton.toggled.connect(Mode)
window.radioButton_2.toggled.connect(Mode)





app.exec()
















