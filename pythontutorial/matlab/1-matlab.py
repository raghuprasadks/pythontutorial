# -*- coding: utf-8 -*-

#https://campus.datacamp.com
#Line plot
import matplotlib.pyplot as plt
year = [1958,1970,1990,2010]
pop=[2.519,3.692,5.263,6.972]
plt.plot(year,pop)
plt.show()

#Scatter plot
import matplotlib.pyplot as plt
year = [1958,1970,1990,2010]
pop=[2.519,3.692,5.263,6.972]
plt.scatter(year,pop)
plt.show()


# Print the last item from year and pop

print(year[-1])

print(pop[-1])


'''
Have another look at the plot you created in the previous exercise; it's shown on the right. Based on the plot, in approximately what year will there be more than ten billion human beings on this planet?
'''
pop[year.index(2085)]

#Histogram

values=[0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,2.6]
plt.hist(values,bins=3)
plt.show()


#Customization
import matplotlib.pyplot as plt
year = [1958,1970,1990,2010]
pop=[2.519,3.692,5.263,6.972]
plt.plot(year,pop)
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Projection')
plt.show()

# bar

# importing matplotlib module  
from matplotlib import pyplot as plt 
  
# x-axis values 
x = [5, 2, 9, 4, 7] 
  
# Y-axis values 
y = [10, 5, 8, 4, 2] 
  
# Function to plot the bar 
plt.bar(x,y) 
  
# function to show the plot 
plt.show() 


# Histogram

# importing matplotlib module  
from matplotlib import pyplot as plt 
  
# Y-axis values 
y = [10, 5, 8, 4, 2] 
  
# Function to plot histogram 
plt.hist(y) 
  
# Function to show the plot 
plt.show() 

#Tics
#Example #1: Default plot

# importing required modules 
import matplotlib.pyplot as plt 
  
# values of x and y axes 
x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50] 
y = [1, 4, 3, 2, 7, 6, 9, 8, 10, 5] 
  
plt.plot(x, y) 
plt.xlabel('x') 
plt.ylabel('y') 
  
plt.show() 

#Example #2: Playing with the ticks
# importing libraries 
import random 
import matplotlib.pyplot as plt 

fig = plt.figure() 

# function to get random values for graph 
def get_graphs(): 
	xs =[] 
	ys =[] 
	for i in range(10): 
		xs.append(i) 
		ys.append(random.randrange(10)) 
	return xs, ys 

# defining subplots 
ax1 = fig.add_subplot(221) 
ax2 = fig.add_subplot(222) 
ax3 = fig.add_subplot(223) 
ax4 = fig.add_subplot(224) 

# hiding the marker on axis 
x, y = get_graphs() 
ax1.plot(x, y) 
ax1.tick_params(axis ='both', which ='both', length = 0) 

# One can also change marker length 
# by setting (length = any float value) 

# hiding the ticks and markers 
x, y = get_graphs() 
ax2.plot(x, y) 
ax2.axes.get_xaxis().set_visible(False) 
ax2.axes.get_yaxis().set_visible(False) 

# hiding the values and displaying the marker 
x, y = get_graphs() 
ax3.plot(x, y) 
ax3.yaxis.set_major_formatter(plt.NullFormatter()) 
ax3.xaxis.set_major_formatter(plt.NullFormatter()) 

# tilting the ticks (usually needed when 
# the ticks are densely populated) 
x, y = get_graphs() 
ax4.plot(x, y) 
ax4.tick_params(axis ='x', rotation = 45) 
ax4.tick_params(axis ='y', rotation =-45) 
	
plt.show() 
