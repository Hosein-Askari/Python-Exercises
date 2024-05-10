class Time :
    def __init__(self,h,m,s) :
        self.hour = h
        self.min = m
        self.sec = s
        self.fix()
        
        
    def fix(self):
        if self.sec>=60 or self.sec < 0:
            self.min += int(self.sec/60)
            self.sec = self.sec % 60
        if self.min >= 60 or self.min<0:
            self.hour += int(self.min/60)
            self.min  = self.min % 60
      
    def sum(self,other):
        new_hour = self.hour + other.hour
        new_min = self.min + other.min
        new_sec = self.sec + other.sec
        new_time = Time(new_hour,new_min,new_sec)
        return new_time
    
    def sub(self,other):
        new_hour = self.hour - other.hour
        new_min = self.min - other.min
        new_sec = self.sec - other.sec
        new_time = Time(new_hour,new_min,new_sec)
        return new_time
    
    def second_to_time(self):
        pass
    #   fix func  do this one.
    


    def time_to_second(self):
        second = self.hour*3600+self.min*60+self.sec
        
        print("seconds : ",second) 
    
    


    def gmt_to_iran (self):
        new_hour =self.hour + 3
        new_min = self.min + 30
        new_time= Time(new_hour,new_min,self.sec)
        return new_time

    def show(self):
        print (f"{self.hour:02d} : {self.min:02d} : {self.sec:02d}")



a=Time(4,5,45)
b=a.gmt_to_iran()
b.show()


