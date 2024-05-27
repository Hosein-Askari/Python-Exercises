import qrcode


class Product :  
    def __init__(self,code,name,price,count) :
        self.code = code
        self.name = name
        self.price = price
        self.count = count

    @staticmethod
    def Add():
        code=input("code : ")
        name=(input("Name : "))
        price=input("Price : ")
        count=input("Count : ")
        new_product=Product(code,name,price,count)
        PRODUCTS.append(new_product)

    
    def Edit(self):
        
        new_input=int(input('''1- Name
2- Price
3- Count
'''))
        match new_input:
            case 1:
                name=input("Name : ")
                self.name=name
            case 2 :
                price=input("Price : ")
                self.price=price
            case 3:
                count=input("Count : ")
                self.count=count
        print("update succesfully")
        
    
    def Remove(self,cnt):

        PRODUCTS.pop(cnt)
        print("delete succesfully")
         
    

    def Buy(self):
        buy_list=[]
        sum = 0
        while(1):
            
            cnt=int(input("how many do yoy want ? "))
            if(int(self.count)>=cnt):
                self.count=str(int(self.count)-cnt)
                my_obj=Product(self.code,self.name,self.price,cnt)
                buy_list.append(my_obj)
                sum += (int(self.price)*cnt)
            else:
                print("we don't have enough ")
            

            choice=input("continue buying ?(Y/N) ")
            if(choice=='N' and sum>0):
                
                print("{:30s}{:30s}{:30s}{}".format("Name","Price","Count","\n"))
                for product in buy_list:
                    for key,item in product.__dict__.items():
                        if key!="code":
                            print("{:30s}".format(str(item)),end ="")
                    print()
                print("{}{:30s}{:30s}".format("\n","Total-price : ",str(sum)))
                break
            elif (choice=='Y'):
                user_input=int(input("enter code : "))
            for product in PRODUCTS:
                if(int(product.code) == user_input):
                    break
            else:
                print("product not found")

    def Qr_code(self):
        
                qcode = qrcode.make(product.__dict__)
                qcode.save("Assignment-12/Store/qrcode.png")

    @staticmethod  
    def Search():
        user_input=input("enter kew-word (name or code): ")
        for product in PRODUCTS:
            if(product.code== user_input or product.name==user_input ):
                print(product.__dict__)
                break
        else:
            print("Product Not found")       


    @staticmethod  
    def Show_list():
        print("{:30s}{:30s}{:30s}{:30s}{}".format("Code","Name","Price","Count","\n"))
        for product in PRODUCTS:
            for key,item in product.__dict__.items():
                print("{:30s}".format(str(item)),end ="")
            print()


class Data_base:


    def Read_data_base(self) : 
        f=open("Assignment-12/Store/database.txt" , "r")

        for line in f:
            result = line.split(',')
            if "\n" in result[3]:

                result[3]=result[3][:-1]
            my_obj = Product(result[0],result[1],result[2],result[3])
            PRODUCTS.append(my_obj)

    def Write_data(self):
        cnt = 0
        f=open("Assignment-12/Store/database.txt" , "w")
        for product in PRODUCTS:
            cnt=0
            for key,item in product.__dict__.items():
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



PRODUCTS=[]

print('''Welcome :) 
      Loading ...''')

data_base = Data_base()
data_base.Read_data_base()

print("data loaded")
while(1):
        
    show_menu()

    user_input=int(input("what do you want do to : "))

    match user_input:
        case 1 :
            Product.Add()
        case 2 :
            user_input=int(input("enter code : "))
            for product in PRODUCTS:
                if(int(product.code)== user_input):
                    product.Edit()
                    break
            else:
                print("product not found")
        case 3 :
            user_input=int(input("enter code : "))
            cnt=0
            for product in PRODUCTS:
                if(int(product.code)== user_input):
                    product.Remove(cnt)
                    del product
                    break
            else:
                print("product not found")
        case 4 :
            Product.Search()
        case 5 :
            Product.Show_list()
        case 6 :
            user_input=input("enter code : ")
            for product in PRODUCTS:
                if product.code == user_input:
                    product.Qr_code()
                    break
            else:
                print("Product Not found")
        case 7 :
            user_input=int(input("enter code : "))
            for product in PRODUCTS:
                if(int(product.code) == user_input):
                    
                    product.Buy()
                    break
            else:
                print("Product Not found")
           
        case 8 :
            data_base.Write_data()
            break



#user_dict = {input(f"Enter key {i+1}: "): input(f"Enter value {i+1}: ") for i in range(num_entries)}
    

# user_dict = {}
 
# num_entries = int(input("Enter the number of entries you want to add: "))
 
# for i in range(num_entries):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     user_dict.update({key: value})
 
# print("Dictionary after adding user input:", user_dict)