import math

def truncate(number, decimals):
    factor = 10 ** decimals
    return int(number * factor) / factor


def f(x):    
    # return x**3 - 0.165 * x**2 + 3.993 * 10**-4
    # return x**4 - 4
    # return 3*x - math.cos(x) - 1
    return x * math.log10(x) - 1.2
def g(x):
    # return 3 * x**2 - 2 * 0.165 * x
    # return 4 * x**3
    # return 3 + math.sin(x)
    return math.log10(x) + (1 / (math.log(10)))


def newton_raphson(x0, decimal_places, max_iter):
    
    error_precision = 10 ** (-decimal_places)

    for i in range(1, max_iter + 1):
        gx = g(x0)
        if gx == 0:
            print("Mathematical Error")
            return None

        x1 = x0 - f(x0) / gx
        if abs(f(x1)) < error_precision and (x1-x0)<error_precision:
            x1_truc = truncate(x1, decimal_places)
            print(f"Root found at x = {x1_truc} after {i} iterations")
            return x1

        x0 = x1

    print("Not Convergent")
    return None


if __name__ == "__main__":
    x0 = float(input("Enter initial guess x0 (e.g. 0.05): "))
    decimal_places = int(input("Enter decimal-place accuracy (e.g. 4): "))
    # max_iter = int(input("Enter maximum number of iterations: "))
    max_iter = 100
    newton_raphson(x0, decimal_places, max_iter)