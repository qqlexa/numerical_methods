# Simple iterations method

try:
    import util
    import matrix
except:
    try:
        from . import util
        from . import matrix
    except:
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
    prev_x = matrix.create_vector(n, 1)

    util.print_equation(a, b)

    matrix.print_vector(x)
    is_found = False
    while not is_found:
        for i in range(n):
            is_found = True
            if abs(x[i] - prev_x[i]) > eps:
                is_found = False
                prev_x[i] = x[i]
                x_ = x[i]
                x[i] += b[i]
                for j in range(n):
                    x[i] += a[i][j] * x_
            matrix.print_vector(x)

    return x


eps = 0.01
student_id = "12648067"
g = int(student_id[-1])  # 7
k = int(student_id[-2])  # 6

eq = [[g + 1, g + 2, g + 3], [2 * (g + 1), g + 6, g - 5], [3 * (g + 1), g, -3]]
eqAd = [k, k + 1, k + 2]

x = solve(eq, eqAd, eps)
print(x)
