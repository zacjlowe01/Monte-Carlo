# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 13:10:19 2026

@author: zacjl

Monte Carlo (Hit & Miss Rectangle Method)
"""

import sympy as sp
import numpy as np
import random
import matplotlib.pyplot as plt

x = sp.symbols('x')

def f(j): 
    f_temp = function.subs(x,j)
    return f_temp


# --- Get values --- #

function = sp.sympify(input("Enter f(x): "))
n = sp.sympify(input("Enter number of random x vales n: "))
a = sp.sympify(input("Enter lower bound a: "))
b = sp.sympify(input("Enter upper bound b: "))
width = b - a
height = sp.maximum(function, x, sp.Interval(a,b))

rectangleArea = sp.sympify(width * height)
xValues = []
yValues = []
tallyUnder = 0

#DEBUG
print("width: ",width)
print("height: ",height)
print("rectangleArea: ",rectangleArea)
print("\nCalculating...")


# --- Generate random points & plot --- #

# Calculate points
sum = sp.sympify(0)
for i in range(n):
    x_rand = random.uniform(a,b)
    y_rand = random.uniform(0,height)
    xValues.append(x_rand)
    yValues.append(y_rand)
    # Keep tally of points that are under vs over the curve 
    if f(x_rand) > y_rand:
        tallyUnder += 1 
  
# Prepare function to be plotted
x_axis = np.linspace(a,b,2*width)
y_axis = []
for i in range(2*width):
    y_axis.append(f(x_axis[i]))

# Plot function and random points
plt.scatter(xValues,yValues,alpha=0.5,s=20)
plt.plot(x_axis,y_axis,linewidth='4')
plt.show()

# Calculate area via ratio
estimatedArea = (rectangleArea*(tallyUnder/n)).evalf()
print("\nEstimated area below the curve:", estimatedArea)

theoretical = sp.integrate(function, (x, a, b))
print("Theoretical value: ",theoretical.evalf())
print("% error: ",(100*abs(estimatedArea-theoretical)/theoretical).evalf())