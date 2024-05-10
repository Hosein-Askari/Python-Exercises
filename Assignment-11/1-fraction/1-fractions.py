class Fraction:
    def __init__(self,n,d) :
        self.numenator = n
        self.denominator = d

        global state 
        state = 1
    global old_n , old_d
    old_n=[0,0]
    old_d=[0,0]

    def sub(self,other):
        old_n [0]=self.numenator
        old_n [1]=other.numenator
        old_d [0]=self.denominator
        old_d [1]=other.denominator
        new_n =self.numenator*other.denominator - other.numenator * self.denominator 
        new_d = self.denominator * other.denominator
        new_fraction = Fraction(new_n,new_d)
        global state
        state = 2
        return new_fraction
    
    def sum(self,other):
        old_n [0]=self.numenator
        old_n [1]=other.numenator
        old_d [0]=self.denominator
        old_d [1]=other.denominator
        new_n =self.numenator*other.denominator + other.numenator * self.denominator 
        new_d = self.denominator * other.denominator
        new_fraction = Fraction(new_n,new_d)
        global state
        state = 3
        return new_fraction


    def mul(self,other):
        old_n [0]=self.numenator
        old_n [1]=other.numenator
        old_d [0]=self.denominator
        old_d [1]=other.denominator
        new_n =self.numenator*other.numenator 
        new_d = self.denominator * other.denominator
        new_fraction = Fraction(new_n,new_d)
        global state
        state = 4
        return new_fraction

    
    def div (self,other):
        old_n [0]=self.numenator
        old_n [1]=other.numenator
        old_d [0]=self.denominator
        old_d [1]=other.denominator
        new_n =self.numenator*other.denominator
        new_d = self.denominator * other.numenator 
        new_fraction = Fraction(new_n,new_d)
        global state
        state = 5
        return new_fraction


    def f_to_n(self):
       
        global state 
        state = 6


    def simp(self):        
        d =[]
        n=[]
        greatest_common_divisor=1
        for i in range(2,self.numenator):
            if self.numenator % i == 0 :
                n.append(i)
            if self.denominator % i == 0 :
                d.append(i)
        for i in n:
            for j in d :
                if i == j and i > greatest_common_divisor:
                    greatest_common_divisor = i
        old_n[0]=self.numenator
        old_d[0] = self.denominator
        self.numenator = int(self.numenator/greatest_common_divisor)
        self.denominator = int(self.denominator/greatest_common_divisor)
        global state 
        state = 7

    def show(self):
      
        match  state :
            case  1  :
                print("\u0332".join("   "+str(self.numenator)+"  "),"\n  ",self.denominator)
            case  2  :
                print("\u0332".join("   "+str(old_n[0])+"  ")," ₋","\u0332".join("   "+str(old_n[1])+"  "),"\u0333".join("  "),
                      "\u0332".join("   "+str(self.numenator)+"  "),"\n  ",old_d[0],"        ",old_d[1],"       ",self.denominator)
            case  3  :
                print("\u0332".join("   "+str(old_n[0])+"  ")," +","\u0332".join("   "+str(old_n[1])+"  "),"\u0333".join("  "),
                      "\u0332".join("   "+str(self.numenator)+"  "),"\n  ",old_d[0],"        ",old_d[1],"       ",self.denominator)
            case  4  :
                print("\u0332".join("   "+str(old_n[0])+"  ")," ×","\u0332".join("   "+str(old_n[1])+"  "),"\u0333".join("  "),
                      "\u0332".join("   "+str(self.numenator)+"  "),"\n  ",old_d[0],"        ",old_d[1],"       ",self.denominator)
            case  5  :
                print("\u0332".join("   "+str(old_n[0])+"  ")," ÷","\u0332".join("   "+str(old_n[1])+"  "),"\u0333".join("  "),
                      "\u0332".join("   "+str(self.numenator)+"  "),"\n  ",old_d[0],"        ",old_d[1],"       ",self.denominator)
            case  6  :
                print("\u0332".join("   "+str(self.numenator)+"  "),"\u0333".join("  "),"{0:.3f}".format(float(self.numenator/self.denominator)),"\n  ",self.denominator)
            case  7  :
                print("\u0332".join("   "+str(old_n[0])+"  "),"\u0333".join("  "),"\u0332".join("   "+str(self.numenator)+"  "),
                      "\n  ",old_d[0],"       ",self.denominator)
                


a=Fraction(12,8)
b=Fraction(7,8)
c = a.sub(b)
c.show()
c.simp()
c.show()