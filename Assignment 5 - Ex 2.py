#importing libraries
import numpy as np
import matplotlib.pyplot as plt

#setting initial variables as given in the question brief
a, b, l = 2, 3, 7
v1, v2 = 299792458,  299792458/2

#creating an array of 1000 evenly spaced values between 0.0 and 8.0. A value
#of 8 was used here as the initial x0 value was 8.
x = np.linspace(0, 8, 1000)

#this set of variables are the gradient descent specific variables
#initial guess x0 of 8, as defined by the question, along with gamma value and
#number of iterations
x0 = 8
gam = 299792458/10
n_iter = 100

#defining a function which will give the time taken for a particular set of 
#parameters (set above) when given a distance x. We only need to return the 
#answer to the equation, so it is entered into the return function
def T(x):
    return(np.sqrt(x**2 + a**2)/v1 + np.sqrt((l-x)**2 + b**2)/v2)

#this function is to verify snells law, it expresses sin(theta_2)/sin(theta_1)
#in terms of x, b, a and l, as we do not know the angles. Numpys trig functions
#were used here.
def verify(x100):
    return(np.cos(np.arctan(b/(l-x100)))/np.cos(np.arctan(a/x100)))

#this function calcualtes the differential of T(x) as it is needed for the grad
#descent part of the code
def df(x):
    return ((x/(v1*(x**2 + a**2)**0.5))-(l-x)/(v2*((l-x)**2 + b**2)**0.5))

#plotting a graph using the x array above and the valuese returned by our 
#function, using a dotted black line to represent the data. 
plt.plot(x, T(x), '--', linewidth=1, color='black')
#labels, titles and legends have been added for clarity
plt.xlabel('Distance x (m)')
plt.ylabel('Time T (s)')
plt.title('Graph of time taken for light to reach B from A for varying distances\n')
plt.legend(['T(x)'])
#using plt.show here tells the program that this is the point where the graph
#should be displayed, allowing for a more digestable format. It will also 
#separate this data from the data to be printed in the second graph.
plt.show()
#here the value given by the brute force method will be displayed. 
#x[np.argmin(T(x))] will find the minimum value of T(x), then this space of the
#array of x will be printed. ie. x[a] where a is the minimum of T(x)
print('Minimizing value of x (by brute force): ', x[np.argmin(T(x))])

#a second graph is plotted here, so far the same as the previous
plt.plot(x, T(x), '--', linewidth=1, color='black')
plt.title('Graph of time taken for light to reach B from A for varying distances\nwith gradient descent plot')
#setting x = x0 to initialise the grad desc algorithm (it would do nothing if
#it started with x=0)
x = x0
#iterating over n_iter (=100) values of i
for i in range (n_iter):    
    #this is the gradient descent algorithm. Gam (gamma) is the learning rate
    #it changes how drastic the gradient of the normal to the function is
    #changed by.
    x = x - gam*df(x)
    #plotting the data onto the graph
    plt.plot(x, T(x), '-o', color='red')
#inserting a legend and stating that this is the point where the graph should
#be output to the console
plt.legend(['T(x)', 'Graidient Descent Best Guess Points',])
plt.show()
#a series of print statements which descibe the results of the code
print(f"Minimizing value of x (by 100 iterations of gradient descent): {x}\n")
print("Verifying Snell's Law:\nsin(\u03F4_2)/sin(\u03F4_1): ", verify(x))
print("v2/v1: ", v2/v1, "\nTherefore, Snell's law has been proven to a good approximation.")

    


