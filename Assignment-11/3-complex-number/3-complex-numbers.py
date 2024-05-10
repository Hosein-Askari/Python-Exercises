class Complex :
    def __init__(self,real,img):
        self.real=real
        self.img = img



    def sum(self,other):
        new_real=self.real + other.real
        new_img = self.img + other.img
        new_complex = Complex(new_real,new_img)
        return new_complex


    def sub(self,other):
        new_real=self.real - other.real
        new_img = self.img - other.img
        new_complex = Complex(new_real,new_img)
        return new_complex
    

#   (a + bi)(c + di) = (ac - bd) + (ad + bc)i 
    def mul(self,other):    
        new_real= self.real * other.real - self.img * other.img
        new_img = self.real * other.img  + self.img * other.real
        new_complex = Complex(new_real,new_img)
        return new_complex
    

    def show(self):
        if self.img >=0 :
            b='+'
        else:
            self.img *= -1
            b='-'
        print(F"{self.real} {b} {self.img}i")
a= Complex(4,5)
b= Complex(7,8)

c=a.mul(b)
c.show()