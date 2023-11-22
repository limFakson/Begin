print("Hello World")

#Variables

name, age = "Fakson", 18
print(name)
print(age)

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

#Dictionariies
Students = {"bob":12, "racheal": 14, "emily":15}
print(Students['racheal'])
#To update the list
Students['racheal'] = 15
print(Students)
#To delete from the dictionaries has same command with list
#same thing with length of the list

#Tuples
#they are immtable - can't be modified
#we use () with them not [] or {}
tup = ('oranges', 'apples', 'bananas')
tup2 = (12,14)
#they can be added together making new tup but can't be modified or changed
tup3 = tup + tup2
print(tup3)

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

#While loops
#It keeps executing while our conditioni is true (i.e it uses condition)
#it uses control statement like: Break, Continue, Pass
#Break - stops the statement prematurly
#Continue - Skips the current litiration and move to the next one
#Pass - is a placeholder that allows one to structure your code without implimenting anything
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