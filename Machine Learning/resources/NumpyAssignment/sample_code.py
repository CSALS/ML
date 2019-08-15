import numpy as np
import time
data = np.random.randn(500,1500)
#generating a 500x1500 matrix; it's upto you to use the dataset

weights = np.random.randn(1,500)
temp=0
out = []
tick = time.time()
for i in range(0,1500):
	temp=0
	for j in range(0,500):
		temp+=weights[0][j]*data[j][i]
	out.append(temp) 
#print(len(out))
tock = time.time() #calculate time taken in seconds
print("Time:",str(tock - tick))
#try to figure out another method to do this in 1 go
#and hence minimize time

