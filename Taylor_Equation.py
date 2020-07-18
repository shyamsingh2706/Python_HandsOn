import sympy as sp
import numpy as np
from sympy.parsing.sympy_parser import parse_expr
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve


# Function to calculate differentiation
def differentiate(exp, n):
    parse = parse_expr(exp)
    # print(parse)
    diff = sp.diff(parse,'a',n)
    # print(diff)
    answer = sp.expand(diff)
    return answer

# Factorial function
def factorial(n):
    if n <= 0:
        return 1
    else:
        return n*factorial(n-1)

# Taylor Equation
def taylor(function,a,x,n):
    i = 0
    p = 0
    while i <= n:

        p = p + ((differentiate(function,i))*((x-a)**i))/factorial(i)

        i += 1
    return p

def calculate_taylor_eq_val(tay_eq,a):

    y = symbols('a')
    print(tay_eq)
    eq = '''"''' + str(tay_eq) + '''"'''
    parse = parse_expr(tay_eq)
    print(parse)
    return parse

# 100 linearly spaced numbers
x = np.linspace(-5,5,100)

# the function, which is y = x^2 /20 here
y = x**2/20
expr = "a**2/20"

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

# plot the Original function
plt.plot(x,y, 'g')
# show the plot
# plt.show()

# validate if differentiation is working fine
# diff_y = differentiate(expr,1)
# print(diff_y)

# validate taylor expression for different order of differentiation
taylor_eq = taylor(expr,2,2.1,1)
print(taylor_eq)

x = calculate_taylor_eq_val(taylor_eq,2)
print(x)

# for a in np.arange(1,5,0.5):
#     min = a - 0.5
#     max = a + 0.5
#     # print(a,min,max)
#     for x in np.arange(min,max,0.1):
#          print(a,min,max,x)
#          taylor_eq = taylor(expr,a,x, 2)