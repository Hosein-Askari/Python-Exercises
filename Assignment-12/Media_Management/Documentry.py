from Media_management import Media




class Documentry(Media):
    def __init__(self,*args):
        super().__init__(*args)
        self.lable='d'



    @staticmethod
    def add(MEDIA): 

        
        name = input("Name : ")
        director = input("director : ")
        imdb = input("imdb : ")
        url = input("url : ")
        x,y = input("duration :(hour and minute with space) ").split()
        if int(y) < 10 :
            y='0'+y        
        duration = x +'h '+y+'m' 
        cast= [i for i in input("cast : (input ',' between names not space)").split(',')]
        my_obj = Documentry(name,director,imdb,url,duration,cast)
        MEDIA.append(my_obj)