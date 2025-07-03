def truncate(number, decimals):
    factor = 10 ** decimals
    return int(number * factor) / factor

def compute_cubic_spline_coefficients(x_points, y_points):
    n = len(x_points)
    a_coeffs = y_points[:]
    h_diffs = [x_points[i+1] - x_points[i] for i in range(n - 1)]

    alpha = [0] * n
    for i in range(1, n - 1):
        alpha[i] = (3 / h_diffs[i]) * (a_coeffs[i+1] - a_coeffs[i]) - (3 / h_diffs[i-1]) * (a_coeffs[i] - a_coeffs[i-1])

    lower = [1] + [0] * (n - 1)
    mu = [0] * n
    z = [0] * n

    for i in range(1, n - 1):
        lower[i] = 2 * (x_points[i+1] - x_points[i-1]) - h_diffs[i-1] * mu[i-1]
        mu[i] = h_diffs[i] / lower[i]
        z[i] = (alpha[i] - h_diffs[i-1] * z[i-1]) / lower[i]

    lower[n-1] = 1
    z[n-1] = 0

    c_coeffs = [0] * n
    b_coeffs = [0] * (n - 1)
    d_coeffs = [0] * (n - 1)

    for j in range(n - 2, -1, -1):
        c_coeffs[j] = z[j] - mu[j] * c_coeffs[j + 1]
        b_coeffs[j] = ((a_coeffs[j+1] - a_coeffs[j]) / h_diffs[j]) - (h_diffs[j] * (c_coeffs[j+1] + 2 * c_coeffs[j]) / 3)
        d_coeffs[j] = (c_coeffs[j+1] - c_coeffs[j]) / (3 * h_diffs[j])

    return a_coeffs[:-1], b_coeffs, c_coeffs[:-1], d_coeffs


def cubic_spline_interpolate(x_points, y_points, x_target, decimal_places):
    a, b, c, d = compute_cubic_spline_coefficients(x_points, y_points)

    # Locate interval for interpolation
    for i in range(len(x_points) - 1):
        if x_points[i] <= x_target <= x_points[i + 1]:
            delta_x = x_target - x_points[i]
            interpolated_value = (
                a[i] +
                b[i] * delta_x +
                c[i] * delta_x**2 +
                d[i] * delta_x**3
            )
            return truncate(interpolated_value, decimal_places)



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
    # n=4
    # x_values=[4,9,16]
    # y_values=[2,3,4]
    # x_interp=7
    # decimal_places=4
    
    interpolated_value = cubic_spline_interpolate(x_values, y_values, x_interp, decimal_places)
    print(f"\nValue at x = {x_interp} is {interpolated_value}")
    
