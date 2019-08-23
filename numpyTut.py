#Never name a file using an existing module name
#https://stackoverflow.com/questions/993984/what-are-the-advantages-of-numpy-over-regular-python-lists
import numpy as np 
#Numpy arrays -> Vectors (1D) , Matrices (2D)
#Numpy arrays better than Python lists

#Creation of numpy arrays

    #From a Python list
my_list = [1,2,3]
numPyVector = np.array(my_list)
print(numPyVector)

my_matrix = [[1,2],[3,4],[5,6]]
numPyMatrix = np.array(my_matrix)
print(numPyMatrix)

    #Using built-in methods
zeroArray = np.zeros(3) #np.ones
print(zeroArray)
zeroMatrix = np.zeros((5,5)) #np.ones
print(zeroMatrix)
rangeArray = np.arange(0,12) #creates array from 0 to 11
print(rangeArray)

    #Random number arrays
randArray1 = np.random.rand(2) # rand -> [0,1)
#np.random.rand(m,n) creates m*n matrix of [0,1)
randArray2 = np.random.randint(1,100) # 1-> low , 100 -> high
randArray3 = np.random.randint(1,100,10) # 10 integers
print(randArray1)
print(randArray2)
print(randArray3)

print(randArray3.max())    #Max ELement 
print(randArray3.argmax()) #Index of Max ELement
print(randArray3.min())
print(randArray3.argmin())

#Functions for Arrays
    
    #The shape attribute for numpy arrays returns the dimensions of the array. 
    #If Y has n rows and m columns, then Y.shape is (n,m) . So Y.shape[0] is n . 
    #shape is a tuple that gives dimensions of the array.

    #BROADCASTING (not available in python lists)
arr = np.arange(0,11)
print(arr)

#Setting a value in a index range from 0 to 4
arr[0:5] = 100
print(arr)

#Slicing
arr = np.arange(0,11)
slice_arr = arr[0:6] #All changes you make in slice_arr get reflected in arr
print(slice_arr)
slice_arr[:] = 101
print(slice_arr)
print(arr)

#Copy
arr = np.arange(0,5)
arr_copy = arr.copy()
slice_arr = arr_copy[0:2]
slice_arr[:1] = 1000
print(slice_arr)
print(arr_copy)
print(arr)


#Operations

#YOu can perform arithmetic operations


