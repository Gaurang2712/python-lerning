#Create a Rectangle class with attributes length and width. Include methods to calculate the area and perimeter of the rectangle.

class Rectangle:
    length=0
    width=0

    def Area(self):
        print("Area of Rectangel is:-",self.length*self.width)
    
    def Perimeter(self):
        print("Area of perimeter is:-",(self.length+self.width)*2)
    
    def addvalue(self,len,wid):
        self.length=len
        self.width=wid

re1=Rectangle()

re1.addvalue(int(input("Enter the length:-")),int(input("Enter the width:- ")))
re1.Area()
re1.Perimeter()