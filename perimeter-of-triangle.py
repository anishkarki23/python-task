#create a class name Triangle.
#create an object from it. The onject will have three attributes named a,b, and c that represent the sides of the triangle.
#The triangle class will  have two methods:
#the init method to initialize the sides
#a method to calculate the perimeter of the triangle from its sides
#the perimeter of the triangle should be printed from outside the class.


class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def  perimeter(self):
        peri = self.a +self.b + self.c
        return peri


        

t1  = Triangle(3,4,5)
result = t1.perimeter()
print(result)

