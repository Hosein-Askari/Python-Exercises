
import math
from functools import partial
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication


loader = QUiLoader()
app = QApplication([])

window = loader.load('Assignment-18/calculator/calculator.ui')

window.show()


x=4
def change( ):
     global x
     choice = x
     match choice:
          case 1 :     
               window .setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(70, 11, 69), stop:1  rgb(204, 31, 204));")
               window.textEdit.setStyleSheet("border-top-left-radius: 25px;border-top-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(78, 12, 76), stop:1  rgb(255, 39, 251));color: rgb(255, 255, 255);")
               window.textEdit_2.setStyleSheet("border-bottom-left-radius: 25px;border-bottom-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(78, 12, 76), stop:1  rgb(255, 39, 251));color: rgb(255, 255, 255);")
               for i in range(1,28):
                    button=f"pushButton_{i}"
                    getattr(window,button).setStyleSheet("""
                         QPushButton:hover {
                                                                                
                         border-radius :25px;
                         background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 rgb(255, 39, 251) , stop: 0.3 rgb(78, 12, 76), stop:0.99  rgb(255, 39, 251));
                         }

                         QPushButton{

                         border-radius :25px;
                         background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(78, 12, 76), stop:1  rgb(255, 39, 251));
                         color: rgb(255, 255, 255);
                         }

                         """ )
          case 2 :     
               window .setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(248, 228, 203), stop:1 rgb(241, 173, 152));")
               window.textEdit.setStyleSheet("border-top-left-radius: 25px;border-top-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 236, 210), stop:0.7 rgb(252, 182, 159));color: rgb(255, 255, 255);")
               window.textEdit_2.setStyleSheet("border-bottom-left-radius: 25px;border-bottom-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 236, 210), stop:0.7 rgb(252, 182, 159));color: rgb(255, 255, 255);")
               for i in range(1,28):
                    button=f"pushButton_{i}"
                    getattr(window,button).setStyleSheet("""
                         QPushButton:hover {

                         border-radius :25px;
                         background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 236, 210), stop:0.4 rgb(252, 182, 159),stop:1 rgb(255, 236, 210));
                         }
                                                                                
                         QPushButton{

                         border-radius :25px;
                         background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 236, 210), stop:0.7 rgb(252, 182, 159));
                         color: rgb(255, 255, 255);
                         }

                         """ )
          case 3 :     
               window .setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(16, 144, 129), stop:0.88 rgb(47, 204, 105));")
               window.textEdit.setStyleSheet("border-top-left-radius: 25px;border-top-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(17, 153, 142), stop:1 rgb(56, 239, 125));color: rgb(255, 255, 255);")
               window.textEdit_2.setStyleSheet("border-bottom-left-radius: 25px;border-bottom-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(17, 153, 142), stop:1 rgb(56, 239, 125));color: rgb(255, 255, 255);")
               for i in range(1,28):
                    button=f"pushButton_{i}"
                    getattr(window,button).setStyleSheet("""
                         QPushButton:hover {
                                                                                
                         border-radius :25px;
                         background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(56, 239, 125), stop:0.4 rgb(17, 153, 142),stop:1 rgb(56, 239, 125));
                         }

                         QPushButton{
                                                                                
                         border-radius :25px;
                         background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(17, 153, 142), stop:1 rgb(56, 239, 125));
                         color: rgb(255, 255, 255);
                         }

                         """ )
          case 4 :     
               window .setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(241, 91, 103), stop:0.95 rgb(240, 180, 106));")
               window.textEdit.setStyleSheet("border-top-left-radius: 25px;border-top-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 95, 109), stop:1 #FFC371);color: rgb(255, 255, 255);")
               window.textEdit_2.setStyleSheet("border-bottom-left-radius: 25px;border-bottom-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 95, 109), stop:1 #FFC371);color: rgb(255, 255, 255);")
               for i in range(1,28):
                    button=f"pushButton_{i}"
                    getattr(window,button).setStyleSheet("""
                         QPushButton:hover {
                                                                                
                         border-radius :25px;
                         background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0  #FFC371, stop:0.4 rgb(255, 95, 109),stop:1 #FFC371);
                         }

                         QPushButton{
                                                                                
                         border-radius :25px;
                         background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(255, 95, 109), stop:1 #FFC371);
                         color: rgb(255, 255, 255);
                         }

                         """ )
          
          case 5 :     
               window .setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(229, 133, 149) , stop:1 rgb(240, 206, 211));")
               window.textEdit.setStyleSheet("border-top-left-radius: 25px;border-top-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 #EE9CA7 , stop:1 #FFDDE1);color: rgb(255, 255, 255);")
               window.textEdit_2.setStyleSheet("border-bottom-left-radius: 25px;border-bottom-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 #EE9CA7 , stop:1 #FFDDE1);color: rgb(255, 255, 255);")
               for i in range(1,28):
                    button=f"pushButton_{i}"
                    getattr(window,button).setStyleSheet("""
                         QPushButton:hover {

                         border-radius :25px;
                         background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0   #FFDDE1, stop:0.4 #EE9CA7 ,stop:1 #FFDDE1);
                         }

                         QPushButton{

                         border-radius :25px;
                         background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 #EE9CA7 , stop:1 #FFDDE1);
                         color: rgb(255, 255, 255);
                         }

                         """ )
          case 6 :     
               window .setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(82, 36, 112) , stop:1 rgb(182, 24, 95));")
               window.textEdit.setStyleSheet("border-top-left-radius: 25px;border-top-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 #662D8C , stop:1 #ED1E79);color: rgb(255, 255, 255);")
               window.textEdit_2.setStyleSheet("border-bottom-left-radius: 25px;border-bottom-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 #662D8C , stop:1 #ED1E79);color: rgb(255, 255, 255);")
               for i in range(1,28):
                    button=f"pushButton_{i}"
                    getattr(window,button).setStyleSheet("""
                         QPushButton:hover {
                                                                                
                         border-radius :25px;
                         background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0   #ED1E79, stop:0.4 #662D8C ,stop:1 #ED1E79);                                                       
                         }

                         QPushButton{

                         border-radius :25px;
                         background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 #662D8C , stop:1 #ED1E79);
                         color: rgb(255, 255, 255);
                         }

                         """ )
          case 7 :     
               window .setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 125, 58) , stop:0.9 rgb(226, 210, 29));")
               window.textEdit.setStyleSheet("border-top-left-radius: 25px;border-top-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 #009245 , stop:1 #FCEE21);color: rgb(255, 255, 255);")
               window.textEdit_2.setStyleSheet("border-bottom-left-radius: 25px;border-bottom-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 #009245 , stop:1 #FCEE21);color: rgb(255, 255, 255);")
               for i in range(1,28):
                    button=f"pushButton_{i}"
                    getattr(window,button).setStyleSheet("""
                         QPushButton:hover {
                                                                                
                         border-radius :25px;
                         background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 #FCEE21 , stop: 0.3 #009245, stop:0.99  #FCEE21);
                         }

                         QPushButton{

                         border-radius :25px;
                         background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 #009245 , stop:1 #FCEE21);
                         color: rgb(255, 255, 255);
                         }""" )
          case 8 :     
               window .setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(188, 22, 80), stop:1 rgb(230, 153, 53));")
               window.textEdit.setStyleSheet("border-top-left-radius: 25px;border-top-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 #D4145A , stop:1 #FBB03B );color: rgb(255, 255, 255);")
               window.textEdit_2.setStyleSheet("border-bottom-left-radius: 25px;border-bottom-right-radius: 25px;background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 #D4145A , stop:1 #FBB03B );color: rgb(255, 255, 255);")
               for i in range(1,28):
                    button=f"pushButton_{i}"
                    getattr(window,button).setStyleSheet("""
                    QPushButton:hover {
                                                                           
                    border-radius :25px;
                    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0,stop:0 #FBB03B , stop: 0.3 #D4145A, stop:0.99  #FBB03B);
                    }

                    QPushButton{

                    border-radius :25px;
                    background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 #D4145A , stop:1 #FBB03B );
                    color: rgb(255, 255, 255);
                    }""" )
     if x==8:
          x=1
     else:
          x += 1   


def text(t):
     
     st = window.textEdit.toPlainText()
     st += t
     
     if '\n' not in st:
          window.textEdit.setText("\n"+st)
     else:
          window.textEdit.setText(st)
def sum():
     global a
     st = window.textEdit.toPlainText()
     a = float(st)
     st += "+"
     window.textEdit_2.setText(st)
     window.textEdit.setText("")

def sub():
     global a
     st = window.textEdit.toPlainText()
     a = float(st)
     st += "-"
     print(a)
     window.textEdit_2.setText(st)
     window.textEdit.setText("")

def mul():
     global a
     st = window.textEdit.toPlainText()
     a = float(st)
     st += "×"
     window.textEdit_2.setText(st)
     window.textEdit.setText("")

def div():
     global a
     st = window.textEdit.toPlainText()
     a = float(st)
     st += "÷"
     window.textEdit_2.setText(st)
     window.textEdit.setText("")


def sin():
     st = window.textEdit.toPlainText()
     b = float(st)
     b=math.sin(math.radians(b))
     window.textEdit_2.setText(f"sin({st})")
     window.textEdit.setText("\n"+str(b))

def cos():
     st = window.textEdit.toPlainText()
     b = float(st)
     b=math.cos(math.radians(b))
     window.textEdit_2.setText(f"cos({st})")
     window.textEdit.setText("\n"+str(b))

def tan():
     st = window.textEdit.toPlainText()
     b = float(st)
     b=math.tan(math.radians(b))
     window.textEdit_2.setText(f"tan({st})")
     window.textEdit.setText("\n"+str(b))

def cot():
     st = window.textEdit.toPlainText()
     b = float(st)
     b=math.tan(math.radians(b))
     b=1/b
     window.textEdit_2.setText(f"cot({st})")
     window.textEdit.setText("\n"+str(b))

def log():
     st = window.textEdit.toPlainText()
     b = float(st)
     b=math.log(b)
     if b - int (b) == 0:
          b= int(b)
     window.textEdit_2.setText(f"log({st})")
     window.textEdit.setText("\n"+str(b))

def sqr():
     st = window.textEdit.toPlainText()
     b = float(st)
     b *= b
     if b - int (b) == 0:
          b= int(b)
     window.textEdit_2.setText(f"sqr({st})")
     window.textEdit.setText("\n"+str(b))

def sqrt():
     st = window.textEdit.toPlainText()
     b = float(st)
     b =math.sqrt(b)
     if b - int (b) == 0:
          b= int(b)
     window.textEdit_2.setText(f"√({st})")
     window.textEdit.setText("\n"+str(b))

def percent():
     st = window.textEdit.toPlainText()
     b = float(st)
     b = b/100 
     if b - int (b) == 0:
          b= int(b)
     window.textEdit_2.setText(str(b))
     window.textEdit.setText("\n"+str(b))


def rev():
     st = window.textEdit.toPlainText()
     b = float(st)
     b *= -1
     if b - int (b) == 0:
          b= int(b)
     window.textEdit.setText("\n"+str(b))

def clear():
     window.textEdit_2.setText("")
     window.textEdit.setText("")


def result():
     st1 = window.textEdit_2.text()
     st2 = window.textEdit.toPlainText()
     
     b = float(st2)
     st2 += "="
     if '+' in st1 :
          c=a+b

     elif '-' in  st1 and '÷' not in st1 and '×' not in st1  :
          c=a-b
          print(a,b)
          
     elif '×' in st1:
          c=a*b
          
     elif '÷':
          c=a/b
          

     
     if c - int (c) == 0:
          c= int(c)
     print(b)
     
     window.textEdit.setText("\n"+str(c))
     window.textEdit_2.setText(st1+st2)


button=[window.pushButton_1,window.pushButton_2,window.pushButton_3,window.pushButton_4,window.pushButton_5,
        window.pushButton_6,window.pushButton_7,window.pushButton_8,window.pushButton_9]
for i in range(0,9):
          button[i].clicked.connect(partial(text,str(i+1)))

window.pushButton_10.clicked.connect(lambda:text("0"))
window.pushButton_11.clicked.connect(lambda:text("."))





window.pushButton_27.clicked.connect(lambda:change())


window.pushButton_12.clicked.connect(lambda:sub())
window.pushButton_13.clicked.connect(lambda:div())
window.pushButton_14.clicked.connect(lambda:mul())
window.pushButton_15.clicked.connect(lambda:sum())

window.pushButton_21.clicked.connect(lambda:sin())
window.pushButton_25.clicked.connect(lambda:cos())
window.pushButton_22.clicked.connect(lambda:tan())
window.pushButton_23.clicked.connect(lambda:cot())
window.pushButton_20.clicked.connect(lambda:log())
window.pushButton_26.clicked.connect(lambda:sqr())
window.pushButton_18.clicked.connect(lambda:sqrt())
window.pushButton_19.clicked.connect(lambda:percent())

window.pushButton_16.clicked.connect(lambda:rev())

window.pushButton_24.clicked.connect(lambda:clear())

window.pushButton_17.clicked.connect(lambda:result())
app.exec()


