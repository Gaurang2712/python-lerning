#106.	Write a C program to find maximum and minimum between two numbers using functions.


class Number:
    a=0
    b=0

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def minmax(self):

        if self.a==self.b:
            print("value is same")

        elif self.a>self.b:
            print("A is max")
        
        else:
            print("B is max")

mynum=Number(10,10)

mynum.minmax()