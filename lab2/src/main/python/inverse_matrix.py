# Inverse matrix method

try:
    import util
    import matrix
except:
    try:
        from . import util
        from . import matrix
    except:
        pass


def solve(a, b):
    """
    :param a: a: matrix, REQUIREMENT: rang(a) should be == n
    :param b: b: matrix (additional)
    :return:  x: vector of solutions
    """
    n = len(a)
    if not matrix.is_square_matrix(a):
        print("It is not possible to find solutions")
        return False

    det = matrix.find_det(a)
    if det == 0:
        # print(f"Error! det == 0")
        return False

    x = matrix.create_vector(n, 0)
    util.print_equation(a, b)

    union_matrix = matrix.find_union_matrix(a)

    union_matrix = matrix.transpose_matrix(union_matrix)

    for i in range(n):
        matrix.mul_row(union_matrix, i, 1 / det)

    for i in range(n):
        for j in range(n):
            x[i] += union_matrix[i][j] * b[j]

    return x

