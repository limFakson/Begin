print("Hello World")

#Variables

name, age = "Fakson", 18
print(name)
print(age)
print(type(age))
print(type(name))

#Arithematic Operations (+, -, /, *, %)
x = 12
y = 18

print(x + y)

#Placeholders
name = "Jake"
sentence = "%s is 15 years old"

print(sentence)
print(sentence % name) #The name is replaces %s in the sentence
#%s is used for strings, while %d is used for integers
# like in:
sentencetwo = "%s is %d years old"
print(sentencetwo  %("Jake", 15))

#list
shopping_list = ['apples', 'bannana', 'oranges', 'cheese']
#To get the first item in the list we locate it with the integer 0, because number starts from zero(0)
print(shopping_list[0]) #it displays the first item in the list 
#slicing of the item
print(shopping_list[0:3])
#Adding an item to an already created list
shopping_list.append('blueberries') #it adds the item to last of the list
#To delete an item from the list 
del shopping_list[1]
print(shopping_list)
#To check the length of itemms 
print(len(shopping_list))
#if we want to filter a list , like remove words with a from the list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for  x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#Dictionariies
Students = {"bob":12, "racheal": 14, "emily":15} 
print(Students['racheal'])
x = Students.keys()
y = Students.values()
#we can also use get() to access a dictionary
#To update the list
Students['racheal'] = 15
print(Students)
#To delete from the dictionaries has same command with list
#we use len() to check the legth of a dctionary
#we can have a list in a dictionary
for i in Students:
    print(i)
    print(Students[i])

#Tuples
#they are immtable - can't be modified
#we use () with them not [] or {}
tup = ('oranges', 'apples', 'bananas')
tup2 = (12,14)
#they can be added together making new tup but can't be modified or changed
tup3 = tup + tup2
print(tup3)

#Set
#To create a set we use {} for em
thisset = {"cat", "tiger", "lion"}
#To access a set we use for loop or search for a variable in it using keyword for and in respectivly
print("dog" in thisset)
#when a set is asked to print an item that not inside a set it prints out false
for x in thisset:
    print(x)
#set rearranges the order of listed item in it
#Add item to a set
thisset.add("leopard")
#item can also be added to a set by updating it from a set, tuple, list or a dictionary
animals = {"dog", "cheetah", "jaguer"}
#let update thisset
thisset.update(animals)
print(thisset)
#We have other means of mergeing two set using union(), intersection_union() or intersection() keeps only the duplicate and dicarding the remaining items in the two sets while symmetric_difference_update() or symmetric_difference() discards the duplicates and keeps the non-duplicates
#to remove an item we use remove() or discard(), we use pop() to remove random item and we use clear() to empty the set but del delete it completely

#Conditional statement
#if, else if, else
if 5>3:
    print("hello")

if 5<3:
    print("hello")
else:
    print("condition not true")
#Relational operations (<,>,>=,<=,==,!=)
age = 16
if age<14:
    print("you are young")
elif age==16:
    print("you are 16")
else:
    print("you are too old")
#and funttions is when a condition is met; or is when either of the conditions are met
#shorthand 
if 3<5: print('correct')
print('correct') if 6<5 else print('incorrect')
#When we use logical operators like and, or, not
#And keyword displays if statement if both coditions are met
#Or keyword if one of the conditions ae correct
#Not if the condition is not correct
a = 300
b = 532
c = 123
if a>c or b<a:
    print('condition is accurate')
else:
    print('You no know book')
#Nested if.....else condition
if a>70:
    print('Above 70')
    if a>95:
        print('Above 95')
    else:
        print('below 95')    

#For loops
list1= ['apples', 'bananas', 'cheeries']
tup1=(2,6,10)
#to print every single item in list1
for item in list1:
    print(item)
for item in tup1:
    print(item)
#using for loops with range 
for i in range(0,10):
    print(i) #it removes/slice thecvery last number in the range
for i in range(0,40,5):
    print(i) #the third number in the range the multiple of numbe to be displayed
#NB: you can nest a loop inside a loop
adj = ['red','green', 'blue']
dic = ['dead', 'immortal', 'ceaser']
for x in adj:
    for y in dic:
        print(x,y)
#NB: we use control statements for both for and while loops
#Break - stops the statement prematurly
#Continue - Skips the current litiration and move to the next one
#Pass - is a placeholder that allows one to structure your code without implimenting anything
#Else - when the codition is no longer met it displays command in else

#While loops
#It keeps executing while our conditioni is true (i.e it uses condition)
#it uses control statement like: Break, Continue, Pass
c = 0
while c<5:
    c = c+1
    print(c)
#the loop will start from the actual value of c which is 0
c=0
while c<5:
    c=c+1
    if c==3:
        break
    print(c)
c=0
while c<5:
    c=c+1
    if c==3:
        continue
    print(c)
c=0
while c<5:
    c=c+1
    if c==3:
        pass
    print(c)

#Try and Except
#if  error occcurs in try python switchs to the except block
try:
    if name>3:
        print(name)
except:
    print("an error occured")

#creating and using functions
#functions are carried out when mentioned. To name a function we use def(define)
def hello_world():
    print("Hello world!")
print(9)
#when not mentioned nothing is printed
hello_world()
def greeting(name):
    print("Hi"+" "+name+" "+'!')
greeting("Fakson")
#the name serves parameter for the function
def add(num1,num2):
    print(num1+num2)
add(10,13)
#25 is printed out showing the parameters are replaced in the last line of the code
#return statement
def add(num1,num2):
    return num1+num2
num_sum = add(12,13)
print(num_sum)

#Built in functions
#They are ready made functions in python like: abs(absolute), bool(truth seeker), dir, help, eval, exec, float.

#Object-Oriented programming(oop)
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def getAge(self):
        return self.age  

p1 = Person('bob',13)
print(p1.getName())
print(p1.getAge())

#Inheritance
class Personal:
    def __init__(self, name, lname):
        self.name = name
        self.lname = lname
    def printname(self):
        print(self.name, self.lname)

f = Personal("Nelson", "Olsen")
f.printname()
class Student(Personal):
    pass

x = Student("Yomi", "Giwa")
x.printname()

#Boolean, Strings
#\ can be used to write an unallowed symbol in a string
print("i am not \"going\"")
#we can change a sting to upper or lower case with
txt = "Daddy's girl"
caps = txt.upper()
print(caps)
lk = txt.lower()
print(lk)
print(txt[2])
#boolen are used to check an operation if true or false
print(bool(5>9))

#Recrusion function
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#Lambda - it can take any number of arguments, but can only have one expression
x = lambda a : a+10
print(x(6))
#the x serves as a parameter holder and lambda decleared the parameters giving it a function
x = lambda a,b : a*b + 11
print(x(3,6))
#Lambda used inside a functioon
def testlamba(e) :
    return lambda a:  a*e
jet = testlamba(3)
print(jet(4))

#Arrays
arrayone = ['ford', 'ganze', 'trefr']
o = arrayone[2] and len(arrayone)
print(o)

#Interators
myset = ('dodo', 'fufu', 'eba', 'ewedu')
inter = iter(myset)
for x in inter:
    print(x)
#Stopinterator
class MyNumbers:
    def __init__(self):
        self.a = 10
    def __iter__(self):
        return self
    def __next__(self):
        if self.a >=8:
            x = self.a
            self.a -= 1
            return x
        else:
            raise StopIteration

myclas = MyNumbers()
myinter = iter(myclas)
for y in myinter:
    print(y)

import datetime
x = datetime.datetime.now()
print(x)

import json
sert= ['feed', 'drive', 'run', 'freak']
x = json.dumps(sert)
print(x)

# #Input attribute - enables user to input data
# Name = input('Enter Name:')
# x = 'Your name is:'
# print(x + ' ' + Name)

#Strings Formatting
quantity = 3
itemno = 567
price = 49
fname = 'Gu He'
myorder = "My name is {3}, I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price, fname))
