import math

def f(x):
    return x**2 -4*x - 10

def truncate(number, decimals):
    factor = 10 ** decimals
    return int(number * factor) / factor

def secant(x0, x1, decimal_places, max_iter):
    
    error_precision = 10 ** (-decimal_places)
    
    f0 = f(x0)
    f1 = f(x1)
    
    if f0 == f1:
        print("f(x0) and f(x1) must be different for secant method.")
        return None


    for i in range(1, max_iter+1):
        
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        f2 = f(x2)
        
        if abs(f2) < error_precision and (x2-x1)<error_precision:
            x2_trunc = truncate(x2, decimal_places)
            print(f"\nRoot found at x = {x2_trunc} after {i} iterations")
            return x2

        
        x0, f0 = x1, f1
        x1, f1 = x2, f2

    
    return x1

if __name__ == "__main__":
    x0 = float(input("Enter first guess x0 (e.g. 4): "))
    x1 = float(input("Enter second guess x1 (e.g. 2): "))
    decimal_places = int(input("Enter how many decimal places accuracy (e.g. 2): "))
    # max_iter = int(input("Enter maximum number of iterations: "))
    max_iter = 100

    secant(x0, x1, decimal_places, max_iter)
