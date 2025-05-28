import sympy as sp
import math

# Step 1: Symbolic variable
x = sp.Symbol('x')

# Step 2: Define the symbolic function
f_expr = x * sp.log(x, 10) - 1.2

# Step 3: Derivative of the function
g_expr = sp.diff(f_expr, x)

# Step 4: Convert symbolic expressions to regular Python functions
f = sp.lambdify(x, f_expr, modules='math')
g = sp.lambdify(x, g_expr, modules='math')

# Example usage
x_val = 2.0
print("f(x) =", f_expr)
print("g(x) =", g_expr)
