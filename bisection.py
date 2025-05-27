import math

def f(x):
    return x**2 * math.sin(x) + math.exp(-x) - 3

def truncate(number, decimals):
    factor = 10 ** decimals
    return int(number * factor) / factor


def bisection(x1, x2, decimal_places, max_iter):
    
    error_precision = 10 ** (-decimal_places)
    x0 = (x1 + x2) / 2
    fx1 = f(x1)
    fx2 = f(x2)

    if fx1 * fx2 >= 0:
        print(f"No root exists between {x1} and {x2}")
        return None

    

    for i in range(1, max_iter + 1):
        x0 = (x1 + x2) / 2
        fx0 = f(x0)


        if abs(fx0) < error_precision and abs(x2-x1)<error_precision :
            m_truc=truncate(x0,decimal_places)
            print(f"\nRoot found at x = {m_truc} after {i} iterations")
            return x0

        if fx1 * fx0 < 0:
            x2 = x0
            fx2 = fx0
        else:
            x1 = x0
            fx1 = fx0

    
    return x0

if __name__ == "__main__":
    
    x1 = float(input("Enter x1 (e.g. 1): "))
    x2 = float(input("Enter x2 (e.g. 2): "))
    decimal_places = int(input("Enter how many decimal places accuracy (eg. 2): "))
    # max_iter = int(input("Enter maximum number of iterations: "))
    max_iter = 100

    bisection(x1, x2, decimal_places, max_iter)
