def truncate(number, decimals):
    factor = 10 ** decimals
    return int(number * factor) / factor

# Define the function and its derivative
def f(x):
    return x**3 - 0.165 * x**2 + 3.993 * 10**-4

def g(x):
    return 3 * x**2 - 2 * 0.165 * x

def newton_raphson(x0, decimal_places, max_iter):
    e = 10 ** -decimal_places
    i = 1

    while i <= max_iter:
        if g(x0) == 0:
            print("Mathematical Error: Derivative is zero.")
            return None

        x1 = x0 - f(x0) / g(x0)

        if abs(f(x1)) <= e:
            root = truncate(x1, decimal_places)
            print(f"Root found: {root}")
            return root

        x0 = x1
        i += 1

    print("Not Convergent")
    return None

# Main block
if __name__ == "__main__":
    try:
        x0 = float(input("Enter initial guess x0: "))
        decimal_places = int(input("Enter how many decimal places accuracy (e.g. 3): "))
        max_iter = int(input("Enter maximum number of iterations: "))
        newton_raphson(x0, decimal_places, max_iter)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
