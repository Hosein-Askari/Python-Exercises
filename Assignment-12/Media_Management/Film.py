from Media_management import Media



class Film(Media):
    def __init__(self,*args):
        super().__init__(*args)
        self.lable='f'
    
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
        my_obj = Film(name,director,imdb,url,duration,cast)
        MEDIA.append(my_obj)

    @staticmethod
    def find_film_a_b(a,b,MEDIA):
        for  media in MEDIA :
            res = [int(i) for i in media.duration if i.isdigit()]
            time = int(res[0])*60+(int(res[1])*10)+int (res[2])
            if time>a and  time<b and media.lable =='f':
                print(media.name)     
