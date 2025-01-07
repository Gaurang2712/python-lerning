# Create a base class Animal with a method make_sound(). 
# Create a derived class Dog that inherits from Animal and implements the make_sound() method to print "Woof!".



class Animal:
    sound=""
    def make_sound(self):
        print(self.sound)

class dog(Animal):
    print('')

d1=dog()

d1.sound="Woof!"
d1.make_sound()

