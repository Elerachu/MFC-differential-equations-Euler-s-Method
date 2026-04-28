# Euler's Method – Ordinary Differential Equation Solver

A Python program that solves Ordinary Differential Equations (ODEs) numerically using Euler's Method.

## How to Run

```bash
python euler_method.py
```

## Sample Output

```
Select a differential equation dy/dx = f(x, y):
  1. f(x, y) = y          (exponential growth: dy/dx = y)
  2. f(x, y) = x + y      (dy/dx = x + y)
  3. f(x, y) = x * y      (dy/dx = x * y)
  4. f(x, y) = x - y      (dy/dx = x - y)
  5. f(x, y) = 2 * x      (dy/dx = 2x, simple integration)

Enter choice (1-5): 1
Solving: dy/dx = y
Enter starting x value: 0
Enter starting y value: 1
Enter step size h: 0.1
Enter final x value: 0.5

Step   x          y               f(x,y)
----------------------------------------------
1      0.1000     1.100000        1.000000
2      0.2000     1.210000        1.100000
3      0.3000     1.331000        1.210000
4      0.4000     1.464100        1.331000
5      0.5000     1.610510        1.464100

Done.
```
