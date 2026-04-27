# ------------------------------------------------
# Program: Solving Differential Equations using Euler's Method
# Description: The Euler method is a first-order numerical procedure
#              for solving ordinary differential equations (ODEs)
#              with a given initial value.
# Method:
#   1. Differential equation: The rule that tells you how y changes with x
#   2. Initial condition: The starting point (x0,y0)
#   3. Step size (h): How far you move along x each time. Smaller = more accurate
#   4. Slope at current point: Rate of change given by the differential equation
#   5. Update values: Use slope and step size to estimate the next point
#   6. Repeat until desired x range is reached
# Formula: y(i+1) = yi + h * f(xi, yi)
#   where i is the current step number
#   y(i+1) is the next y value
#   yi is the current y value
#   xi is the current x value
#   h is the step size
# ------------------------------------------------

# Get user inputs
x = float(input("Enter starting x value: "))  # starting x value
y = float(input("Enter starting y value: "))  # initial condition y(x0)
h = float(input("Enter step size h: "))        # size of each step
x_end = float(input("Enter final x value: "))  # where to stop

# Calculate number of steps
n = int((x_end - x) / h)  # total steps = range / step size

# Euler's method loop
for i in range(n):
    y_new = y + h * y  # apply Euler's formula: y_new = y + h * f(x,y)
    x = x + h          # move x forward by one step
    y = y_new          # update y for next iteration
    print(f"x = {x:.2f}, y = {y:.4f}")  # print current values