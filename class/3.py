#  Implement a Student class with attributes for name, roll number, and marks in three subjects. 
# Add methods to calculate the total marks and average marks.

class Student:
    name=""
    rollnumber=0
    sub1=0
    sub2=0
    sub3=0

    def addvalue(self,n,r,s1,s2,s3):
        self.name=n
        self.rollnumber=r
        self.sub1=s1
        self.sub2=s2
        self.sub3=s3
    
    def totalmarks(self):
        # total=0
        # for i in self.marks:b
        #     total=total+i
        print("total of sub",self.sub1+self.sub2+self.sub3)

std1=Student()
std1.addvalue(input("Enter Student Name:-"),int(input("Enter Student RollNumber:-")),int(input("Sub1 marks:-")),int(input("Sub1 marks:-")),int(input("Sub1 marks:-")))

std1.totalmarks()