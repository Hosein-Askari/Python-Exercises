from Media_management import Media




class Clip(Media):
    def __init__(self,*args):
        super().__init__(*args)
        self.lable='c'


    @staticmethod
    def add(MEDIA): 

        
        name = input("Name : ")
        director = input("director : ")
        imdb = input("imdb : ")
        url = input("url : ")
        x,y = input("duration :(minute and second with space) ").split()       
        duration = x +'m '+y+'s' 

        cast= [i for i in input("cast : (input ',' between names not space)").split(',')]
        my_obj = Clip(name,director,imdb,url,duration,cast)
        MEDIA.append(my_obj)