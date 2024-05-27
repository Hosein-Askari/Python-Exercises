from Media_management import Media
from Film import Film
from Series import Series
from Clip import Clip
from Documentry import Documentry
from Actor import ACTORS





def Read_data_base() : 
    f=open("Assignment-12/Media_Management/database.txt", "r")

    for line in f:
        result = line.split(',')
        if "\n" in result[-1]:
            result[-1]=result[-1][:-1]
        if result[0]=="film" :
            my_obj = Film(result[1],result[2],result[3],result[4],result[5],result[6:])
            MEDIA.append(my_obj)
        elif result[0]=="series" :
            my_obj = Series(result[6],result[1],result[2],result[3],result[4],result[5],result[7:])
            MEDIA.append(my_obj)
        elif result[0]=="documentry" :
            my_obj = Documentry(result[1],result[2],result[3],result[4],result[5],result[6:])
            MEDIA.append(my_obj)
        elif result[0]=="clip" :
            my_obj = Clip(result[1],result[2],result[3],result[4],result[5],result[6:])
            MEDIA.append(my_obj)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def Write_data():
    f=open("Assignment-12/Media_Management/database.txt", "w")
    f.write("Movies\n")
    for media in MEDIA:

        match media.lable:
            case 'f' :
                f.write("film,")
            case 's' :
                f.write("series,")
                str=""
            case 'f' :
                f.write("documentry,")
            case 'f' :
                f.write("clip,")
        for key,item in media.__dict__.items():
            if media.lable=='s':
                
                if( isinstance(item, list)):
                    for arg in item:
                        
                        if(arg == item[len(item)-1]):
                            str += arg.full_name
                        else:
                            str += arg.full_name+','
                elif (key!="lable"  ) :
                    f.write(item+',')    
            else:
                if( isinstance(item, list)):
                    for arg in item:
                        
                        if(arg == item[len(item)-1]):
                            f.write(arg.full_name)
                        else:
                            f.write(arg.full_name+',')
                elif (key!="lable" ) :
                        f.write(item+',')
        if len(str)>1 :
            f.write(str)
            str=""  
        f.write("\n")


    f.write("\nActors\n")
    for actor in ACTORS:
        
        for key,item in actor.__dict__.items():
            if( isinstance(item, list)):
                    for arg in item:
                        
                        if(arg == item[len(item)-1]):
                            f.write(arg)
                        else:
                            f.write(arg+',')
            else :
                    f.write(item+',')     
        f.write("\n")
    f.close

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

MEDIA = []

Read_data_base()



x=int(input('''////////////////MENU////////////////////
        1-Add_media
        2-Show_info
        3-Download-media
        4-Movie with special duration 
        what do you wanna do?'''))

match x :
    case 1:
        type = input("what kind of media you wanna add?(series/film/documentry/clip) ")
        match type:
            case "series":
                Series.add(MEDIA)
            case "film" :
                Film.add(MEDIA)
            case "documentry" :
                Documentry.add(MEDIA)
            case "clip" :
                Clip.add(MEDIA)
    case 2:
        n=input("input name of media : ")
        Media.show_info(n,MEDIA)
    case 3:
        n=input("input name of media : ")
        Media.download(n,MEDIA)
    case 4 :
        a1,a2 = map(int,input("input min-time (hour and minute with space) ").split())
        b1,b2 =map(int,input("input max-time (hour and minute with space) ").split())
        a=a1*60+a2
        b=b1*60+b2
        Film.find_film_a_b(a,b,MEDIA)



Write_data()