# ------------------------------------------------
# Program: Solving Differential Equations using Euler's Method
# Description: The Euler method is a first-order numerical procedure for solving ordinary differential equations (ODEs) with a given initial value.
# Method:
# 1. Differential equation: The rule that tells you how y changes with x
# 2. Initial condition: The starting point (x0,y0)
# 3. Step size (h): How far you move along x each time. Smaller = more accurate
# 4. Slope at current point: Rate of change given by the differential equation
# 5. Update values: Use slope and step size to estimate the next point
# 6. Repeat until desired x range is reached
# Formula: y(i+1) = yi + h * f(xi, yi)
#   where i is the current step number
#         y(i+1) is the next y value
#         yi     is the current y value
#         xi     is the current x value
#         h      is the step size
# ------------------------------------------------


# --- def means we are creating a reusable block of code called a "function" ---
# --- This function shows the menu and returns the equation the user picks ---
def get_ode():

    # print() displays text on the screen for the user to read
    print("\nSelect a differential equation dy/dx = f(x, y):")
    print("  1. f(x, y) = y          (exponential growth: dy/dx = y)")
    print("  2. f(x, y) = x + y      (dy/dx = x + y)")
    print("  3. f(x, y) = x * y      (dy/dx = x * y)")
    print("  4. f(x, y) = x - y      (dy/dx = x - y)")
    print("  5. f(x, y) = 2 * x      (dy/dx = 2x, simple integration)")

    # input() pauses the program and waits for the user to type something
    # whatever they type gets saved in the variable called "choice"
    choice = input("\nEnter choice (1-5): ")

    # if/elif/else checks what the user typed and runs the matching block
    # "lambda x, y:" is a shorthand way to write a small math function
    # e.g. lambda x, y: x + y means "given x and y, return x + y"
    # We return TWO things: the math function, and a label describing it
    if choice == "1":
        return lambda x, y: y, "dy/dx = y"           # f(x,y) = y
    elif choice == "2":
        return lambda x, y: x + y, "dy/dx = x + y"   # f(x,y) = x + y
    elif choice == "3":
        return lambda x, y: x * y, "dy/dx = x * y"   # f(x,y) = x * y
    elif choice == "4":
        return lambda x, y: x - y, "dy/dx = x - y"   # f(x,y) = x - y
    elif choice == "5":
        return lambda x, y: 2 * x, "dy/dx = 2x"      # f(x,y) = 2x
    else:
        # If the user types anything other than 1-5, use equation 1 as default
        print("Invalid choice. Defaulting to dy/dx = y")
        return lambda x, y: y, "dy/dx = y"


# --- Call the function above and store what it returns ---
# f        = the math function the user selected (used later to calculate slope)
# ode_label = the text label e.g. "dy/dx = y" (used for display only)
f, ode_label = get_ode()

# Show the user which equation is being solved
print(f"\nSolving: {ode_label}")


# --- Get the starting values from the user ---
# float() converts the typed text into a decimal number
x     = float(input("Enter starting x value: "))  # x0: where we begin on the x-axis
y     = float(input("Enter starting y value: "))   # y0: the known value of y at x0
h     = float(input("Enter step size h: "))         # h: how big each step is (smaller = more accurate)
x_end = float(input("Enter final x value: "))       # where to stop calculating


# --- Work out how many steps are needed to get from x to x_end ---
# Example: x=0, x_end=1, h=0.1 → (1-0)/0.1 = 10 steps
# int() removes any decimal, round() fixes small floating point errors
n = int(round((x_end - x) / h))


# --- Print the column headers for the results table ---
# The :<6, :<10 etc. control how wide each column is so everything lines up neatly
print(f"\n{'Step':<6} {'x':<10} {'y':<15} {'f(x,y)':<15}")
print("-" * 46)  # prints a line of 46 dashes to separate the header from the data


# --- This loop runs Euler's Method one step at a time ---
# range(n) counts from 0 up to n-1, so the loop runs exactly n times
for i in range(n):

    # Calculate the slope at the current point using our chosen equation
    # f is the function we selected earlier e.g. f(x,y) = x + y
    slope = f(x, y)

    # Apply Euler's formula: move y forward using the slope
    # new y = old y + (step size × slope)
    y = y + h * slope

    # Move x forward by one step size
    # round(..., 10) prevents tiny floating point errors from building up
    # e.g. 0.1 + 0.1 + 0.1 in Python can become 0.30000000000000004
    x = round(x + h, 10)

    # Print the results for this step in a neat table row
    # i+1 is the step number (we add 1 because i starts at 0)
    # .4f means show 4 decimal places for x
    # .6f means show 6 decimal places for y and slope
    print(f"{i+1:<6} {x:<10.4f} {y:<15.6f} {slope:<15.6f}")


# --- All steps are done ---
print("\nDone.")
