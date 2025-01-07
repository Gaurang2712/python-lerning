# Create a base class Device with a method turn_on(). 
# Create derived classes Laptop and Smartphone that inherit from Device and 
# implement the turn_on() method to print "Laptop is on" and "Smartphone is on", respectively.


class Device:
    type=''
    def turn_on(self):
        print(f'{self.type} is on')
    
class Laptop(Device):
    pass

class Smartphone(Device):
    pass