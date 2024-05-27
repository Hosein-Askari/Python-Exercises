from Media_management import Media;



class Series(Media):
    def __init__(self,p,*args):
        super().__init__(*args)
        self.parts = p
        self.lable='s'

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
        part=input("parts : ")
        cast= [i for i in input("cast : (input ',' between names not space)").split(',')]
        my_obj = Series(part,name,director,imdb,url,duration,cast)
        MEDIA.append(my_obj)