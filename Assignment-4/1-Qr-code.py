import qrcode

name = input(" name : ")
cellphone = input("cellphone : ")

code= qrcode.make(name + '\n' + cellphone )
code.save("qrcode.png")