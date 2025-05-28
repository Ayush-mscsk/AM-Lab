import matplotlib.pyplot as plt
import numpy as np

# Function and its derivative
def f(x):
    return x**3 - 0.165 * x**2 + 3.993e-4

def g(x):
    return 3 * x**2 - 2 * 0.165 * x

# Truncate function
def truncate(number, decimals):
    factor = 10 ** decimals
    return int(number * factor) / factor

# Plot after each iteration
def plot_iteration(x0, x1, iteration):
    x_vals = np.linspace(x0 - 0.01, x0 + 0.1, 400)
    y_vals = f(x_vals)
    tangent_line = f(x0) + g(x0) * (x_vals - x0)

    plt.figure(figsize=(6, 4))
    plt.plot(x_vals, y_vals, 'r', label='Function f(x)')
    plt.plot(x_vals, tangent_line, 'b--', label='Tangent line at x0')
    plt.axvline(x=x0, color='g', linestyle='-', label='x0 (Current root)')
    plt.axvline(x=x1, color='orange', linestyle='-', label='x1 (Next root)')
    plt.axhline(0, color='black', linewidth=0.5)

    plt.title(f"Newton-Raphson Iteration {iteration}")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()  # Blocking call - should display every time

# Newton-Raphson with plotting
def newton_raphson(x0, decimal_places, max_iter):
    e = 10 ** -decimal_places

    for i in range(1, max_iter + 1):
        gx = g(x0)
        if gx == 0:
            print("Mathematical Error: Derivative is zero")
            return None

        x1 = x0 - f(x0) / gx

        plot_iteration(x0, x1, i)  # Show plot

        abs_error = abs((x1 - x0) / x1) * 100
        if abs_error < 5:  # Absolute relative error threshold
            x1_trunc = truncate(x1, decimal_places)
            print(f"\nRoot found at x = {x1_trunc} after {i} iterations")
            return x1_trunc

        x0 = x1

    print("Not Convergent")
    return None

# Main script
if __name__ == "__main__":
    try:
        x0 = float(input("Enter initial guess x0 (e.g., 0.05): "))
        decimal_places = int(input("Enter decimal place accuracy (e.g., 4): "))
        max_iter = 100
        newton_raphson(x0, decimal_places, max_iter)
    except Exception as e:
        print("Error:", e)
