#Strongly typed language -> Checks the data type of variable
#Weakly typed language -> Doesn't check data type.. Data Type can be changed any time for the same variable
#Python doesn't require semicolon to end statements

#PRINT & INPUT FUNCTION -> INBUILT IN PYTHON

#Print Statement
print ("HELLO WORLD! ")
print('x' * 3) #Before printing expression is evaluated

#Taking INPUT
name = input('What is your name? ')
print(name)
print(type(name)) #PRINTS DATA TYPE
#1.Variables
i = 42
#String literals '' , "" , ''' '''(for multi-line)
name = "Charan"
print (name)
print (name[1:-1]) #Substring starting from 1st char till -1th char (excluding that)
name = 'Sai'
print (name)
multLine = '''
Hi man,
How are yu doing?
'''
message = "HELLO WORLD MAN"
words = message.split(' ') # At ' ' string separated into words

#Arrays are called Lists in Python . Index stars from 0 , End Index stars from -1 
emptyArray = []
array1 = [1,"HELLO"]
array2 = [1,2,3,4,5,6]
print(array2[3:]) #array2[:] is assumed as array2[0:]
length = len(array2) #LENGTH OF ARRAY
array2.append(7) #APPENDING TO ARRAY
array2.insert(6,10)
array1.clear() #EMPTIES OUR LIST
array2.remove(10)
array2.pop() #REMOVES LAST ITEM
indexOfFirstOccurence = array2.index(5)
print(50 in array2)
array2.append(5)
countOfFives = array2.count(5)
array2.sort() 
#None -> Object in python that represents absence of a value
print(array2)
array2.reverse()
array3 = array2.copy()
print(array3)

#2D LIST -> MATRIX
matrix = [
    [1,2,3] ,
    [4,5,6] ,
    [7,8,9]
]
for row in matrix:
    for item in row:
        print(item)


#Loops
#1.WHILE
count = 1
while(count < 3):
    print(count)
    count = count + 1 #count++ IS INVALID

#2.FOR LOOP (for in)
newArray = [10,20,30]
for i in newArray:
    print(i)
newString = "Charan"
for c in newString:
    print(c)

#3.Iterating by Index of Sequences (for in)
newArray = [100,200,300]
for index in range(len(newArray)):
    print(newArray[index])

# ; allows multiple statements on single line




#No braces for code block instead here use indentation

#Conditional Statement
if True:
    print ("TRUE")
else:
    print ("FALSE")

#FUNCTIONS

#declaring
def speak_something():
    print("HELLO MAN.How you're doing")
#calling
speak_something()

def printHi(name):
    print(f'HELLO {name} !')
printHi("charan sai")

def square(number):
    return number*number
print(square(4))


#EXCEPTIONS

try:
    age = int(input('Age: '))
    print(age)
except ValueError: #what errors might occur
    print('Invalid Age Value')


#MODULES
#dividing code into different files
#each file is called module which can re-used anywhere

#Importing entire module
import moduleBasic #moduleBasic is object

print(moduleBasic.sayHello())

#Importing specific functions in the module
import moduleBasic
from moduleBasic import sayHello
sayHello()


#PACKAGES

#Related modules contained in one package (basically a folder)
#To create a package , create a folder and create a file named __init__
#Interpreter treats the directory as package if __init__.py is present

#importing a module in a package
    #one way (import entire module in a package)
import ecommer.shipping 
ecommer.shipping.calc_shipping()

    #second way (importing functions from a module in package)
from ecommer.shipping import calc_shipping, calc_tax
calc_shipping()

    #third way (importing specific module from package)
from ecommer import shipping


#Python standard libary has many modules
#python package index directory -> pypi we can find many packages which we can use
#to install
#pip install <packageName> 
#pip -V to see which directory pip installs external packages to

# With `npm`, packages are installed locally by default and automatically recorded in your `package.json` manifest.
#  In Python, packages are installed globally by default and no such automatic manifest exists.
#  Conventionally, Python developers will write the results of `pip freeze` into a file named `requirements.txt` in the root of the project, but `pip` won't 
#  update this file for you when you install new packages, unfortunately. This gets added and committed to source control, just like `package.json`, and 
#  the `pip install` command accepts such a file with the `-r` flag. It's a manual process

