

class Actor():
    def __init__(self,n,h,w,a,e,*args):
        self.full_name = n
        self.height = h
        self.weight = w
        self.age = a
        self.eye_color = e
        self.movies = []
        for arg in args:
            for i in arg:
                 self.movies.append(i)




ACTORS =[]

f=open("Assignment-12/Media_Management/database.txt" , "r")
flag = False
for line in f:
    result = line.split(',')
    if "\n" in result[-1]:
        result[-1]=result[-1][:-1]

    if flag :
            if  len(result)>1:
                my_obj = Actor(result[0],result[1],result[2],result[3],result[4],result[5:])
                ACTORS.append(my_obj)
    if result[0] == "Actors":
        flag =True 
        
    