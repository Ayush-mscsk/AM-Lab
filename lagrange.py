def truncate(number, decimals):
    factor = 10 ** decimals
    return int(number * factor) / factor

def lagrange_interpolation(x_values, y_values, x, decimal_places):
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    result_trunc = truncate(result, decimal_places)
    return result_trunc

if __name__ == "__main__":
    n = int(input("Enter number of data points: "))

    x_values = []
    y_values = []

    print("Enter x and y values separated by space:")
    for _ in range(n):
        x, y = map(float, input().split())
        x_values.append(x)
        y_values.append(y)

    x_interp = float(input("Enter the value of x to interpolate: "))
    decimal_places = int(input("Enter number of decimal places accuracy: "))

    interpolated_value = lagrange_interpolation(x_values, y_values, x_interp, decimal_places)
    print(f"\nValue at x = {x_interp} is {interpolated_value}")
