
time = input()
hour = ""
min = ""
sec = ""
for i in range (len(time)):
    if (time[i]==':'):
        hour +=time[i-2]
        hour += time[i-1]
        hour = int(hour)
        min  += time[i+1]
        min  += time[i+2]
        min = int (min)
        sec  += time[i+4]
        sec  += time[i+5]
        sec = int (sec)
        result = (hour * 3600) + (min *60) + sec
        break
    
print(result)
