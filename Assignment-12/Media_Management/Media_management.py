from pytube import YouTube 
from Actor import ACTORS


class Media:
    def __init__(self,n,d,i,u,du,*args):
        self.name = n
        self.director = d
        self.IMDB_score = i
        self.url = u
        self.duration = du
        self.cast = []
        for arg in args:
            for i in arg :
                for a in ACTORS:
                    if a.full_name == i :
                        self.cast.append(a)
                        
    @staticmethod
    def download(name,MEDIA):
   
        for media in MEDIA:
            if media.name == name:
                url = media.url
                break;
        link = url

        try: 
            # object creation using YouTube 
            yt = YouTube(link) 
        except: 
        
            print("Connection Error")       

        mp4_streams = yt.streams.get_by_resolution(360)

        try: 
        
            mp4_streams.download()
            print('Video downloaded successfully!')
        except: 
            print("Some Error!")




   


            
    @staticmethod
    def show_info(name,MEDIA):
        for media in MEDIA:
            if media.name == name :
                for key,item  in media.__dict__.items() :
                    
                    if( isinstance(item, list)):
                        print("cast : ",end="")
                        for arg in item:
                            
                            if(arg == item[len(item)-1]):
                                print(arg.full_name)
                            else:
                                print(arg.full_name,end=',')
                    elif (key!="lable") :
                        print(key,":",item)    
                            
                        
    