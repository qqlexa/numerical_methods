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


def solve(a, b, eps=0.01):
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

    x = [0 for i in range(n)]
    for j in range(n):
        x[j] = round(b[j] / a[j][j], 3)

    prev_x = [1 for i in range(n)]

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
