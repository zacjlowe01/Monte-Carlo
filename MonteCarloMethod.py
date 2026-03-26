# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:11:59 2026

@author: zacjl

Monte Carlo Numerical Integration
"""

import sympy as sp
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
xValues = []
yValues = []


# --- Calculate area --- #

# Sum f evaluated at n random numbers within the interval
sum = sp.sympify(0)
for i in range(n):
    n_rand = random.randint(a,b)
    f_rand = f(n_rand)
#    xValues.append(n_rand)
#    yValues.append(f_rand)
    sum += sp.sympify(f_rand)

avgHeight = sum/n
Area = (avgHeight*width).evalf()
print("Average height within the interval: ", (avgHeight).evalf())
print("Area: ",Area)


# Calculate function symbolically
theoretical = sp.integrate(function, (x, a, b))
print("Theoretical value: ",theoretical.evalf())
print("% error: ",(100*abs(Area-theoretical)/theoretical).evalf())