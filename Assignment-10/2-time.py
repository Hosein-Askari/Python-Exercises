class Time :
    def __init__(self,h,m,s) :
        self.hour = h
        self.min = m
        self.sec = s
      
    def sum(self):
        pass
    
    def sub(self):
        pass
    
    

    def time_to_second(self):
        second = self.hour*3600+self.min*60+self.sec
        
        print("seconds : ",second) 

    def show(self):
        print (f"{self.hour:02d} : {self.min:02d} : {self.sec:02d}")



