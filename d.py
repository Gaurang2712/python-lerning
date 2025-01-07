================================================
File: /conditional_statements.py
================================================
# true and false
# conditional statements decide the flow of the program based on the condition given.

name = "Gumit"

# if else
if (name=="Sumit"):
    print("Hello Sumit")
else:
  print("Hello Other")

isLogin = True

if(isLogin):
  print("Welcome")
else:
  print("Please login")

# if elif else

a = 12
b = 20
c = 13

if a>b:
  print("a is less than b")
elif(a>c):
  print("a is greater than c")
elif(a==c):
  print("a equals c")
elif(a!=c):
  print("a is not equal to c")
else:
  print("other")

# nested if else

x = 12
y = 10
z = 30

if x>y:
  if(x<z):
    print("x is less than z")
  else:
    print("x is greater than z")
else:
  if(y>z):
    print("y is greater than x and z")






================================================
File: /datatypes.py
================================================
# datatypes in python

# int # non decimal

num1 = 1034343434434
print(num1)
print(type(num1))

# float # decimal

num2 = 10.123456789
print(num2)
print(type(num2))

# complex

num3 = 1 + 2j
print(num3)
print(type(num3))

# str

str1 = "bascom bridge"
print(str1)
print(type(str1))

# bool

isLogin = False
print(isLogin)
print(type(isLogin))

# single line comment

"""  multiline comment
sadadsadsad
sad
sadsadsa
dsa
dsa
dsadsad
"""


================================================
File: /dictionary_datatype.py
================================================
# dictionary datatypw is a collection of key-value pairs
userData = {              # json
  "name":"Sumit",
  "age":30,
  "email":"sumit@gmail.com",
  "marks":[70,80,90],
  (1,2,3):"tuple as key",
  "isStudent":True,
  "address":{
    "city" : "New York",
    "state" : "NY",
    "country" : "USA"
  },
  "name":"Gumit",
}


"""

"{              # json
  "name":"Sumit",
  "age":30,
  "email":"sumit@gmail.com",
  "marks":[70,80,90],
  (1,2,3):"tuple as key",
  "isStudent":True,
  "address":{
    "city" : "New York",
    "state" : "NY",
    "country" : "USA"
  },
}"


"""

print(userData)
print(type(userData))
print(userData["name"])
print(userData["address"]["city"])

userData["address"]["city"] = "Pune"

print(userData)

print(len(userData))

# set and dictionary are unordered
values = {}                    # dictionary
print(type(values))

# empty set
values = set()
print(type(values))

userData["height"] = 12.3

print(userData)

# popitem()
userData.popitem()
print(userData)

# pop()
userData.pop("name")
print(userData)


# clear() empty the dictionary

# copty and = same as before

# items()  keys()  values()
print()
print(userData.items())
print()
print(userData.keys())
print()
print(userData.values())


================================================
File: /fstring.py
================================================
a = 10
print("Value of a is",a)

print(f"value of a is {a}")

print(f"value is {"hi" if a <10 else "bye"}")

# print the multiplication table of 13

num = int(input("Enter a number: "))

for i in range(1,11):
  print(f"{num} * {i} = {num*i}")


print("Hi",end=" ")
print("Hello")


================================================
File: /functions.py
================================================
# functions
# function is block of code that runs when we called it

# function name
# function parameter
# function body
# function return value

# lambda function (anonymous function)(function without name)

def geet():
  print("Hello world")

geet()
geet()
geet()
geet()
geet()

# function with parameter

def geet():
  print("Hello", "Public")

geet()
geet()
geet()
def congrats(name):
  print("Hello", name)

congrats("Arpit")
congrats("Rohan")
congrats("Raj")

def add(n1,n2,n3,n4):
  print("Sum is : => ",n1+n2+n3+n4)

add(1,2,3,4)
add(5,6,7,8)
add(7,8,9,0)


def ra1():
  return 12.34

# if function is returning something the function becomes a variable

print(ra1())
b = ra1()
print(b)

result = 10 + ra1()
print(result)

# with paramter and with return type

def returnRange(start,end):
  list = []
  for i in range(start,end+1):
    list.append(i)
  return list

print(returnRange(1,10))


# for i in returnRange(1,10):
#   print(i)

##################################################################################

# arbitary arguments
# with the use of arbitary arguments we can pass any number of arguments to the function

def take(*args):
  print(args)
  print(args[5])


take(1,12,13,15,16,7,8,9,10)

# keyword arguments

def person(name,age,address):
  print("Name is : ",name)
  print("Age is : ",age)
  print("Address is : ",address)

person(address="Delhi",name="Arpit",age=23)

# default arguments

def sum(a,b=10):
  print(a+b)

sum(12,12)

# keyword arbitary arguments

def company(**kwargs):
  print(kwargs)

company(name="Google",ceo="Sundar Pichai",founder="Larry Page",location="Mountain View",industry="Technology",noOfEmployees=1000,year=1998)



================================================
File: /intro.py
================================================
# python programming
# highlevel programming language
# easy to learn
# interpreted language

# 0101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010

# compiler and interpreter (c // c++)
# highlevel => lowlevel

# compiler
# highlevel // c => intermediate language => lowlevel (010101)

# interpreter
# line by line execution

# IDE - integrated development environment

print("hello world")


================================================
File: /lambda_functions.py
================================================
# lambda functions
# lambda function is anonymous function(function without name)

# def sum(a,b):
#   return a+b


result =  lambda a,b : a+b

print(result(12,12))

# lambda function is used to create a higher order function
# higher order function is a function which takes function as a parameter
# or returns a function as a result

def func(data):
  print(data(10))

func(lambda x : x+10)   # function as parameter (lambda function in a parameter)


def calculation(a,b,func):

  print(func(a,b))

calculation(10,20,lambda x,y : x/y)

# lambda function is used to extends the functionality of a function

def maruFunction():
  return lambda a : a+10

print(maruFunction()(10))

# numpy library has a function called "vectorize" which can be used to convert a function to a vectorized function

# map function
nums = [1,6,9,7,4,3,6,8,9,6,4,4]  # 12


# for i in range(0,len(list)):
#   list[i] = list[i] + 10

print(list)

res= map(lambda x : x*10,nums)

print(list(res))


================================================
File: /list_datatype.py
================================================
# squencial data types
# group of values under a single variable name
# 1. list
# 2. tuple
# 3. set
# 4. dict

# list # []
# ordered, mutable ,indexed, allows duplicates

numbers = [1, 2, 3, 4, 5,6,7,8,"Bascom",True,23.343,12 + 3j]
#          0  1  2  3  4
print(numbers)
print(type(numbers))

print(len(numbers))

fruits = ["apple", "banana", "cherry"]
print(fruits)

# accessing elements in list
print(numbers[8])

print(numbers[8:12])   # : range operator

newList = numbers[8:12]
print(newList)

print(numbers[-1])

print(numbers[-12:-8])

print(numbers[0:5:2])  # start : end+1 : step

print(numbers[:4])

print(numbers[4:])

print(numbers[5::2])

# chnage elements in list
height = [12.3, 14.5, 16.7, 18.9]
height[1] = 17.7
print(height)

height[2:4] = [19.9,19.0]
print(height)

# insert elements in list
height.insert(2,999.99)
print(height)

height.append(1000.00)
print(height)

weight = [12.3, 14.5, 16.7, 18.9]
height.extend(weight)
print(height)

# remove elements from list
height.remove(1000.00)
print(height)

height.pop()
print(height)

height.pop(1)
print(height)

# sort the list
height.sort(reverse=False)
print(height)

# copy one list into another
list1= [1,2,3]
list2 = []

list2 = list1

print(list2)

list2[1] = 100
print(list2)

print(list1)

list3 = []
list3 = list1.copy()

print(list3)
list3[1] = 200
print(list3)
print(list1)

# + operator between list
l1 = [1,2,3]
l2 = [4,5,6]
# l3 = l1 + l2
l1.extend(l2)
print(l1)

# empty the list
l1.clear()
print(l1)

# find index of value
l1 = [1,2,3,4,5,6]
print(l1.index(4))

# reverse the list
l1.reverse()
print(l1)

# count the number of occurrences of a value in list
l1 = [1,2,3,4,5,6,2,3,4,5,2,2]
print(l1.count(2))





================================================
File: /loop_inside_loop.py
================================================
# loop inside loop

for i in range(1,6):
  for j in range(1,6):
    print("*",end="")
  print()

for i in range(1,6):
  for j in range(1,i+1):
    print("*",end="")
  print()




================================================
File: /loops.py
================================================
# loops in python

# for loop
# while

# num = int(input("Enter a number: "))  # 100
# num = 10

for i in range(1,11): print(i)

for i in range(1,11,2): # start,end+1,step
  print(i)

for i in range(10,2,-1):  # for reverse loop
  print(i)

# print all the odd number between 1 and 1000

for i in range(1,1001): print(i) if i % 2 == 1 else None

# while
a = 1

while a<10:
  print(a)
  a+=1


================================================
File: /operators.py
================================================
# operators are the symbols that represent computations like addition and multiplication.

# arithmetic operators

# + - * /  %(modulus)   **(power) //(integer division)
a = 10
b = 20
print(a+b) # addition
print(a-b) # subtraction
print(a*b) # multiplication
print(a/b) # division

c = a/b
print(type(c))

# % modulus reminer

print(12 % 5)  # 0
print(7 % 12)

""" (get the last digit of a number)
12 % 10 = 2
1234 % 10 = 4

"""

# // integral division
print(100//3)

# ** power
print(2**3)
print(3**2)


############### conditional operators ####################

# < > <= >= == !=  # gives boolean value True or False

a = 10
b = 25

print(a<b)
c = a>b
print(type(c))

print(a==b)
print(a!=b)

############### logical operators ####################

# and or not # multiple conditions # True or False

"""
and operator: truth table
True and True = True
True and False = False
False and True = False
False and False = False

or operator: truth table
True or True = True
True or False = True
False or True = True
False or False = False

not operator: truth table
not True = False
not False = True
"""

a = 10
b = 50

print(not(a<b or b > 100))


# assignment operator  # =
# += -= *= /= %= //= **=

num = 12

num += 5
# num = num + 5
print(num)

num %= 55
print(num)

# num = num + 1  # there is no ++ or -- operator in python


================================================
File: /range_in_operator.py
================================================
# in operator
numbers = [1,2,3,4,5]

# if(userInput in numbers):
#   print("Your number is in the list")
# else:
#   print("Your number is not in the list")

# range operator
# 1 to 100

if((int(input("Enter a number: "))) in range(1,101)):
  print("Your number is in the range")
else:
  print("Your number is not in the range")

# if else one liner

# num = 12
# if num<10:
#   print("less than 10")
# else:
#   print("greater than or equal to 10")

print("less than 10") if (int(input("Enter a number: ")))<10 else print("greater than or equal to 10")


# None if there is no else in one liner if else


================================================
File: /set_datatype.py
================================================
# set
# unordered, mutable, no duplicates

numbers = {1, 12, 3, 4, 99,5, 6, 7, 8, 9, 10,1,2,3}
print(numbers)
print(type(numbers))

# insert value in set
numbers.add(11)
print(numbers)

values = {77,66,55}
numbers.update(values)
print(numbers)

# remove and discard
numbers.discard(100)
print(numbers)

numbers.pop()
print(numbers)


set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
# print(set1.union(set2))
print(set1 | set2)
# print(set1.intersection(set2))
print(set1 & set2)
print(set1.difference(set2))
print(set1 - set2)

# forzen set
frozen_set = frozenset({1,2,3,4,5})
print(frozen_set) # readonly set

tuple1 = tuple(set1)  # also usig typecasing


================================================
File: /tuple_datatype.py
================================================
# tuple is a collection of elements of different data types
# tuple is immutable # unchangeable # readonly
# indexed # ordered # allows duplicates
# ()

vegitables = ('carrot', 'potato', 'tomato', 'onion', 'pepper')
# vegitables[0] = 'cabbage'  not possible in tuple

print(vegitables[0])
print(vegitables[1])

print(len(vegitables))

print(type(vegitables))

vegitables = list(vegitables)

print(type(vegitables))
vegitables[0] = 'cabbage'
print(vegitables)

vegitables = tuple(vegitables)
print(vegitables)


================================================
File: /type_casting.py
================================================
# type casting

a = 10
print(type(a))

f = float(a)  # type casting from int to float
print(type(f))
print(f)

height = 12.3
print(type(height))

height_int = int(height)
print(type(height_int))
print(height_int)

# str
str = "100"
print(type(str))

str_int = int(str)
print(type(str_int))
print(str_int)

# bool
isLogin = False
print(type(isLogin))

isLogin_int = int(isLogin)
print(type(isLogin_int))
print(isLogin_int)

# int to bool
num = 3
num_bool = bool(num)
print(type(num_bool))
print(num_bool)

# float to bool
num = 0.0
num_bool = bool(num)
print(type(num_bool))
print(num_bool)

# str to bool
str = ""           # false for empty string
str_bool = bool(str)
print(type(str_bool))
print(str_bool)


================================================
File: /user_input.py
================================================
# input()

name = float(input("Please enter your name: "))
print(name)



================================================
File: /variables.py
================================================
# data => ram
# variable name to give data or store data into ram
a = 12
# a is a variable name and 12 is the data stored in ram
b = 13

# rules for variable names:
# 1. a-z, A-Z, 0-9, _ (underscore)
# 2. can't start with a number
# 3. can't use keywords

a1 = 12
a_1 = 13
_e4 = 14

print(a1)
print(a_1)
print(_e4)


================================================
File: /oopc/assign_value_using_function.py
================================================
class Bank:
  name = ""
  accountNumber = 0
  type=""
  balance = 0

  def assignValues(self,name,accountNumber,type,balance):  # assign properties using function
    self.name = name
    self.accountNumber = accountNumber
    self.type = type
    self.balance = balance

  def display(self):    # print function to display properties
    print("Name:",self.name)
    print("Account Number:",self.accountNumber)
    print("Type:",self.type)
    print("Balance:",self.balance)

  def enjoy(self):
    print("Enjoy your life today 31st Dec")


b1 = Bank()
b1.assignValues("SBI",123456789,"savings",10000)
b1.display()


b2 = Bank()
b2.assignValues("HDFC",987654321,"current",20000)
b2.display()

b3 = Bank()
b3.enjoy()


================================================
File: /oopc/circle_program.py
================================================
# create class called Circle with attributes radius and color
# create method called area and circumference which calculates the area of the circle and circumference of the circle respectively

class Circle:
  radius = 0
  color = ""

  def assignValues(self, r, col):
    self.radius = r
    self.color = col

  def findArea(self):
    print("The area of the circle is:", 3.14 * self.radius * self.radius)

  def findCircumference(self):
    print("The circumference of the circle is:", 2 * 3.14 * self.radius)


c1 = Circle()
c1.assignValues(int(input("Enter the radius of the circle: ")),
                input("Enter the color of the circle: "))
c1.findArea()
c1.findCircumference()


================================================
File: /oopc/class_object.py
================================================
# class object
# oopc
# object oriented programming concepts
# functional programming
# object oriented programming  # dividing a code into classes and objects

# class
# object

class Student:  # blueprint

  # properties(variables) # methods(memer functions)
  # multiple datatypes under single variable name

  name= ""
  age = 0
  marks = []


  def learning(self):
    print("students are learning")

s1 = Student()  # object
s1.name = "Arpit"
s1.age = 23
s1.marks = [12,34,56,78]

s2 = Student()
s2.name = "John"
s2.age = 24
s2.marks = [12,34,56,78]

s3 = Student()
s3.name = "John"
s3.age = 24
s3.marks = [12,34,56,78]

s4 = Student()


for i in [s1,s2,s3,s4]:
  print(i.name, i.age, i.marks)
  i.learning()




================================================
File: /oopc/oopc_into.py
================================================
# oopc
# object oriented programming concepts
# class
# object
# constrcutor
# inheritance
# polymorphism  # more then one form
# abstraction
# encapsulation

def add(a,b):
  return a+b

def add(a,b,c):
  return a+b+c

print(add(1,2,3))

import tkinter as tk

root = tk.Tk()
root.mainloop()



# (tkinter)tkinter
# api calling
# mongodb
# database connectivity
# email // whatsapp
# django


================================================
File: /programs/chrismas_tree_pattern.py
================================================
for i in range(1,6):

  # space
  for j in range(1,6-i):
    print(" ",end="")

  # star
  for j in range(1,2*i):
    print("*",end="")

  print()

for i in range(1,3):
  print(" "*3,"|")

print("---------")
print("Mara Yashu")


================================================
File: /programs/prime.py
================================================
# prime number

# num = int(input("Enter a number: ")) # 13  # 2..12


# print("Numer from user is",num)

# flag = 1

# for i in range(2, num):
#   if num%i==0:
#     flag = 0
#     break

# if flag == 1:
#   print("Number is prime")
# else:
#   print("Number is not prime")

# 55
# 2..54

num = int(input("Enter a number: "));flag = 1

for i in range(2, num):
    if num % i == 0:
        flag = 0
        break

print("Number is prime") if (flag == 1)  else print("Number is not prime")







