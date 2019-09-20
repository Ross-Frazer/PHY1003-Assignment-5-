#importing libraries
import numpy as np
import matplotlib.pyplot as plt

#defining function called ls_best_fit which takes two values, x and y.
def ls_best_fit (x, y):
    
    #I split up the equation into multiple parts as it felt easier to code. It also fixed an
    #error I was recieving previously. Once each part is calculated separately the final
    #equation m is calculated. This equation is to find the least squares fitting of a set
    #of data x and y.
    #numpy has built in mean functions which are used here
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    top = (x - x_mean)*(y - y_mean)
    bottom = (x - x_mean)**2
    sum_top = np.sum(top)
    #numpy has built in sum functions which are used here
    sum_bottom = np.sum(bottom)
    m = sum_top/sum_bottom

    #as we have found the gradient above we now must find the y-axis intercept
    #this is a reaarranged version of the linear equation y=mx+c
    c = y_mean - m*x_mean

    #this function returns a gradient m and an intercept c
    return (m, c)

#this is the raw data which is given, I kept this separate to make it easier to
#change the data if needed. numpys array function is used here as we can then
#apply mathematical operators to it.
x_raw = np.array([9.3, 7.0, 8.6, 6.7, 5.5, 9.0, 7.3, 7.4, 8.3, 7.7])
#here we create a new array where every x_raw value is squared
x = x_raw**2
y = np.array([1500, 700, 1200, 800, 450, 1200, 850, 900, 1000, 800])

#here I am calling upon my function, passing it the values in arrays x and y
#I am assinging m and c to the values returned.
m, c = ls_best_fit(x, y)
#here the line of best fit is being calculated
line = m*x + c
#this block of code uses matplotlib to plot the graph, various attributes are
#defined and axis are labelled.
plt.plot(x, y, 'o', color='red')
plt.plot(x, line, '-', linewidth=1, color='black')
plt.xlabel('radius$^2$ (cm$^2$)')
plt.ylabel('mass (g)')
plt.title('Graph of suqare of radius of pie against mass with trendlines')

#to calculate a theoretical value an idealised case is created
rad_theor = np.linspace(30, 90, 100)
#a theoretical value is calculated using numpys built in pi function to compare
#with the value found above. 
m_theor = 1*(np.pi)*(rad_theor)*5
#this theoretical data set is plotted on the same graph to highlight the difference
plt.plot(rad_theor, m_theor, '--', linewidth=1, color='blue')
plt.legend(['Pies', 'Least squares data', 'Theoretical masses of pies'])
plt.show()
#here an estimate of pi is printed
print('Using a gradient of m =', m, ', and an intercept of c =', c, ', an estimate of pi was calculated to be: ', m/(1*5), 'which is the mass divided by the product of the density and the height.')