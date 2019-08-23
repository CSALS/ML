# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 06:33:55 2019

@author: Charan
"""

#Matplotlib is the "grandfather" library of data visualization with Python
#It is an excellent 2D and 3D graphics library for generating scientific figures.
import matplotlib.pyplot as plt
#USE THIS LINE TO SEE PLOTS IN JUPYTER NOTEBOOKS %matplotlib inline
#FOR OTHER EDITORS plt.show()

#For plot.show() opened in new window use the following 2 statements
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt')

#Plotting 2 NumPY Arrays
import numpy as np
x = np.arange(0,10)
y = x ** 2

plt.plot(x,y,'ro')  #ro -> red circles , r -> red line , defualt is b- -> blue line
plt.xlabel('This is X-AXIS label')
plt.ylabel('This is Y-AXIS label')
plt.title('Give the title of plot here')
plt.show()

#Plotting mutiplots on same graph
plt.plot(x,x,'r--',x,y,'r')
plt.show()

