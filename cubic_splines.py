def truncate(number, decimals):
    factor = 10 ** decimals
    return int(number * factor) / factor

def cubic_spline_coefficients(x, y):
    n = len(x)
    a = y[:]
    h = [x[i+1] - x[i] for i in range(n-1)]

    # Set up the system of equations
    alpha = [0] * n
    for i in range(1, n-1):
        alpha[i] = (3/h[i])*(a[i+1] - a[i]) - (3/h[i-1])*(a[i] - a[i-1])

    l = [1] + [0]*(n-1)
    mu = [0]*n
    z = [0]*n

    for i in range(1, n-1):
        l[i] = 2*(x[i+1] - x[i-1]) - h[i-1]*mu[i-1]
        mu[i] = h[i]/l[i]
        z[i] = (alpha[i] - h[i-1]*z[i-1])/l[i]

    l[n-1] = 1
    z[n-1] = 0

    c = [0]*n
    b = [0]*(n-1)
    d = [0]*(n-1)

    for j in range(n-2, -1, -1):
        c[j] = z[j] - mu[j]*c[j+1]
        b[j] = (a[j+1] - a[j])/h[j] - h[j]*(c[j+1] + 2*c[j])/3
        d[j] = (c[j+1] - c[j]) / (3*h[j])

    return a[:-1], b, c[:-1], d

def cubic_spline_interpolation(x_values, y_values, x_interp, decimal_places):
    a, b, c, d = cubic_spline_coefficients(x_values, y_values)

    # Find the right interval
    for i in range(len(x_values) - 1):
        if x_values[i] <= x_interp <= x_values[i + 1]:
            dx = x_interp - x_values[i]
            result = a[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3
            return truncate(result, decimal_places)

    raise ValueError("Interpolation point is outside the given range.")

if __name__ == "__main__":
    # n = int(input("Enter number of data points: "))

    # x_values = []
    # y_values = []

    # print("Enter x and y values separated by space:")
    # for _ in range(n):
    #     x, y = map(float, input().split())
    #     x_values.append(x)
    #     y_values.append(y)

    # x_interp = float(input("Enter the value of x to interpolate: "))
    # decimal_places = int(input("Enter number of decimal places accuracy: "))
    n=4
    x_vals=[4,9,16]
    y_vals=[2,3,4]
    x_interp=7
    decimal_places=4
    
    interpolated_value = cubic_spline_interpolation(x_vals, y_vals, x_interp, decimal_places)
    print(f"\nValue at x = {x_interp} is {interpolated_value}")
    
