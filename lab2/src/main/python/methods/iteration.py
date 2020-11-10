# Simple iterations method
# http://matica.org.ua/metodichki-i-knigi-po-matematike/vychislitelnaia-matematika-praktikum/1-2-1-metod-prostoi-iteratcii-metod-iakobi

try:
    import util
    import matrix
except:
    try:
        from . import util
        from . import matrix
    except:
        pass


def count_array(a, b, i, i2):
    if a[i][i] != 0:
        if a[i2][i] != 0:
            number = float(a[i2][i] / a[i][i])
            matrix.mul_row(a, i, number)
            b[i] *= number
            # util.print_equation(a, b)
            matrix.row_minus_row(a, from_i=i2, minus_i=i)
            b[i2] -= b[i]
        else:
            # print(f"a[{i2}][{i}] == 0")
            pass
    else:
        # print(f"a[{i}][{i}] == 0")
        pass


def solve(a, b, eps):
    """
    :param a:   matrix, REQUIREMENT: rang(a) should be == n
    :param b:   matrix (additional)
    :param eps: calculation error
    :return x:  vector of solutions
    """
    n = len(a)
    if not matrix.is_square_matrix(a):
        print("It is not possible to find solutions")
        return False

    x = matrix.create_vector(n, 0)
    for j in range(n):
        x[j] = round(b[j] / a[j][j], 3)

    prev_x = matrix.create_vector(n, 1)

    util.print_equation(a, b)

    is_found = False
    iterations = 1
    while not is_found:
        for i in range(n):
            is_found = True
            if abs(x[i] - prev_x[i]) > eps:
                is_found = False
                prev_x[i] = x[i]
                x[i] = b[i]
                for j in range(n):
                    if j != i:
                        x[i] -= round(a[i][j] * prev_x[j], 4)
                x[i] = round(x[i] / a[i][i], 4)
        iterations += 1

    return x, iterations


eps = 0.0001
student_id = "12648067"
g = int(student_id[-1])  # 7
k = int(student_id[-2])  # 6

# eq = [[g + 1, g + 2, g + 3], [2 * (g + 1), g + 6, g - 5], [3 * (g + 1), g, -3]]
# eqAd = [k, k + 1, k + 2]

eq = [[24, 14, -8.1], [16, 26, 5.4], [8, 18, 27]]
eqAd = [8, 7, 6]
coefficient = [1, 2, 2.7]

x, iterations = solve(eq, eqAd, eps)
for i in range(len(x)):
    x[i] *= coefficient[i]

print(x)

"""eps = 0.01
 eq = [[20.9, 1.2, 2.1, 0.9], [1.2, 21.2, 1.5, 2.5], [2.1, 1.5, 19.8, 1.3], [0.9, 2.5, 1.3, 32.1]]
 eqAd = [21.7, 27.46, 28.76, 49.72]

x = solve(eq, eqAd, eps)
print(x)
"""
