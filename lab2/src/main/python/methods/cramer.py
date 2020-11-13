# Cramer method

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

    x = [0 for i in range(n)]

    new_matrix = [[j for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if k == j:
                    new_matrix[i][j] = b[i]
                else:
                    new_matrix[i][j] = a[i][j]
        x[k] = matrix.find_det(new_matrix) / det
    return x
