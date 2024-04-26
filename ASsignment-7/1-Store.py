import qrcode

def Read_data_base() : 
    f=open("ASsignment-7\database.txt","r")

    for line in f:
        result = line.split(',')
        if "\n" in result[3]:

            result[3]=result[3][:-1]
        my_dict={"Code":result[0],"Name":result[1], "Price":result[2], "Count":result[3]}
        PRODUCTS.append(my_dict)

def Write_data():
    cnt = 0
    f=open("ASsignment-7\database.txt","w")
    for product in PRODUCTS:
        cnt=0
        for key,item in product.items():
            if(cnt<3):
                f.write(item+',')
            elif(cnt==3):
                f.write(item)
            cnt += 1
        f.write("\n")
    f.close

def show_menu():
    print('''/////////////////Menu///////////////////
      
      1- Add
      2- Edit 
      3- Remove
      4- Search
      5- Show-list
      6-Qr-code
      7- Buy
      8_ Exit''')



def Add():
    code=int(input("code : "))
    name=(input("Name : "))
    price=input("Price : ")
    count=int(input("Count : "))
    new_product={"Code":str(code),"Name":name, "Price":price, "Count":str(count)}
    PRODUCTS.append(new_product)










def Edit():
    user_input=int(input("enter code : "))
    for product in PRODUCTS:
        if(int(product["Code"])== user_input):
            new_input=int(input('''1- Name
2- Price
3- Count
'''))
            match new_input:
                case 1:
                    name=input("Name : ")
                    product["Name"]=name
                case 2 :
                    price=input("Price : ")
                    product["Price"]=price
                case 3:
                    count=input("Count : ")
                    product["Count"]=count
            print("update succesfully")
            break
    
    print("Product not found")





def Remove():

    user_input=int(input("enter code : "))
    cnt=0
    for product in PRODUCTS:
        if(int(product["Code"])== user_input):
            PRODUCTS.pop(cnt)
            print("Product succesfully removed")
            break
        cnt += 1
    else:
        print("Product not found")


def Search():
    user_input=input("enter kew-word : ")
    for product in PRODUCTS:
        if(product["Code"]== user_input or product["Name"]==user_input ):
            print(product)
            break
    else:
        print("Product Not found")       



def Show_list():
    print("{:30s}{:30s}{:30s}{:30s}{}".format("Code","Name","Price","Count","\n"))
    for product in PRODUCTS:
        for key,item in product.items():
            print("{:30s}".format(str(item)),end ="")
        print()


def Qr_code():
    user_input=int(input("enter code : "))
    for product in PRODUCTS:
        if(int(product["Code"])== user_input):
            qcode = qrcode.make(product)
            qcode.save("qrcode.png")
            break
    else:
        print("Product Not found")

def Buy():
    buy_list=[]
    sum = 0
    while(1):
        user_input=int(input("enter code : "))
        for product in PRODUCTS:
            if(int(product["Code"])== user_input):
                cnt=int(input("how many do yoy want ? "))
                if(int(product["Count"])>=cnt):
                    product["Count"]=str(int(product["Count"])-cnt)
                    my_dict={"Name":product["Name"],"Price":product["Price"],"Count":str(cnt)}
                    buy_list.append(my_dict)
                    sum += (int(product["Price"])*cnt)
                    break
                else:
                    print("we don't have enough ")
        else:
            print("Product Not found")

        choice=input("continue buying ?(Y/N) ")
        if(choice=='N' and sum>0):
            
            print("{:30s}{:30s}{:30s}{}".format("Name","Price","Count","\n"))
            for product in buy_list:
                for key,item in product.items():
                    print("{:30s}".format(str(item)),end ="")
                print()
            print("{}{:30s}{:30s}".format("\n","Total-price : ",str(sum)))
            break
PRODUCTS=[]

print('''Welcome :) 
      Loading ...''')

Read_data_base()

print("data loaded")
while(1):
        
    show_menu()

    user_input=int(input("what do you want do to : "))

    match user_input:
        case 1 :
            Add()
        case 2 :
            Edit()
        case 3 :
            Remove()
        case 4 :
            Search()
        case 5 :
            Show_list()
        case 6 :
            Qr_code()
        case 7 :
            Buy()
        case 8 :
            Write_data()
            break



#user_dict = {input(f"Enter key {i+1}: "): input(f"Enter value {i+1}: ") for i in range(num_entries)}
    

# user_dict = {}
 
# num_entries = int(input("Enter the number of entries you want to add: "))
 
# for i in range(num_entries):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     user_dict.update({key: value})
 
# print("Dictionary after adding user input:", user_dict)