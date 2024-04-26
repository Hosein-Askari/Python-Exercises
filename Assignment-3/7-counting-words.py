str = input(" enter sentenses : ")
count_chars = [' ', ',' , ';' ,'(',')','.']
count = 0 
i=0
flag = False
while (i<len(str)):
    
    
        if str[i] in count_chars :
        
        
            if(i+1 != len(str)):
                for j in range (i+1,len(str)):
                    if str[j] not in count_chars :
                        count += 1
                       
                        i=j
                        
                        break
                    else :
                        i += 1
            else:
                i += 1
        else:
            i += 1
    

if (str[0] not in count_chars):
    count += 1
   
print (count)