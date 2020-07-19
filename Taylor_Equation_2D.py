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


# Function to return Taylor Equation
def taylor(function,a,x,n):
    i = 0
    p = 0
    while i <= n:

        p = p + ((differentiate(function,i))*((x-a)**i))/factorial(i)

        i += 1
    return p

# function to Calculate value of Taylor equation for a value of a
def calculate_taylor_eq_val(tay_eq,input_val):

    x = symbols('a')
    y = tay_eq.subs(x,input_val)
    return y



def taylorExpVal(fX,xvalue,avalue):
    f0 = fX.subs(x, xvalue)
    print(f0)
    sum = f0
    for i in range(1,3):
        equation = sym.diff(fX, x)
        newterm = (equation.subs(x, xvalue)) / math.factorial(i)
        xadiff = (xvalue-avalue)**i
        newterm = newterm * xadiff
        sum += newterm
    return sum



# 100 linearly spaced numbers
x = np.linspace(-5,5,100)

# the function, which is y = x^2 /20 here
y = x**2/20
expr = "a**2/20"

# setting the axes at the centre
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
# plot the Original function
plt.plot(x,y, 'g')

ty_graph_axis=[]
ty_graph_axis_x = []
ty_graph_axis_y = []
Order_of_diffrential = 3

 # create range of A for step of .5 and then plot of each "X" as 0.1 step for every "a" range
for a in np.arange(0,5,0.5):
    min = a - 0.5
    max = a + 0.5
    # print(a,min,max)
    for x in np.arange(min,max,0.1):
         taylor_eq = taylor(expr,a,x,Order_of_diffrential)
         y = calculate_taylor_eq_val(taylor_eq,a)
         Taylor_plot_axis = [x,y]
         ty_graph_axis_x.append(x)
         ty_graph_axis_y.append(y)
         ty_graph_axis.append(Taylor_plot_axis)

# Plot taylor Expansion Graph
for ty_axis in ty_graph_axis:

    ax.plot(np.linspace(0,float(ty_axis[0])),np.linspace(0,float(ty_axis[1])))

# Plot both the graph together ( original and taylor Graph )
ax.plot(ty_graph_axis_x,ty_graph_axis_y,'r')
plt.show()

