# Create a base class Shape with a method draw(). 
# Create derived classes Circle and Square that inherit from Shape and 
# implement the draw() method to print "Drawing Circle" and "Drawing Square", respectively.


class Shape:
    def draw(self,type):
        self.type=type
        print(f'Drawing {self.type}')

class Circle(Shape):
    pass

class Square(Shape):
    pass

c1=Circle()
c1.draw('Circle')


s1=Square()
s1.draw('Square')


