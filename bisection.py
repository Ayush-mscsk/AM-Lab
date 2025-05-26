import math

def f(x):
    return x**2 * math.sin(x) + math.exp(-x) - 3

def truncate(number, decimals):
    factor = 10 ** decimals
    return int(number * factor) / factor


def bisection(a, b, decimal_places, max_iter):
    
    error_precision = 10 ** (-decimal_places)
    m = (a + b) / 2
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        print(f"No root exists between {a} and {b}")
        return None

    print(f"\n{'n':<5}{'a':<20}{'b':<20}{'m':<20}{'f(m)':<20}")
    print("-" * 90)

    for i in range(1, max_iter + 1):
        m = (a + b) / 2
        fm = f(m)


        if abs(fm) < error_precision :
            
            print(f"\nRoot found at x = {truncate(m,decimal_places)} after {i} iterations")
            return m

        if fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm

    
    return m

if __name__ == "__main__":
    
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    decimal_places = int(input("Enter how many decimal places accuracy (eg. 3): "))
    max_iter = int(input("Enter maximum number of iterations: "))

    bisection(a, b, decimal_places, max_iter)
