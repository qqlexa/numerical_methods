# Gauss matrix method
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


def solve(a, b):
    """
    :param a: a: matrix
    :param b: b: matrix (additional)
    :return:  x: vector of solutions
    """
    n = len(a)
    if isinstance(a, list) and isinstance(b, list) and n == len(b):
        for i in a:
            if len(i) != len(b):
                print("Incorrect data")
                return
    else:
        return

    x = matrix.create_vector(n, 0)
    util.print_equation(a, b)

    for i in range(n):
        for i2 in range(i + 1, n):
            count_array(a, b, i, i2)
        # util.print_equation(a, b)

    for i in range(n - 1, -1, -1):
        for i2 in range(i - 1, -1, -1):
            count_array(a, b, i, i2)
        # util.print_equation(a, b)

    for i in range(n):
        if a[i][i] != 0:
            x[i] = b[i] / a[i][i]
        else:
            print(f"Error! a[{i}][{i}] == 0")
            return False
    print(x)
    return x


if __name__ == '__main__':
    solve([[20, 10], [17, 22]], [350, 500])
