# Gauss matrix method
import matrix
import util


def find_max_in_array(a, c, i1, i2=-1):
    """
    :param a: matrix
    :param c: vector of positions
    :param i1: row of finding
    :param i2: row of finding
    :return: tuple (i, j)
    """
    if i2 == -1:
        i2 = len(a)
    max_number = a[i1][c[i1]]
    max_i = i1
    max_j = 0
    for i in range(i1, i2):
        for j in range(i1, i2):
            if max_number < a[i][j]:
                max_number = a[i][j]
                max_i = i
                max_j = j
    return max_i, max_j


def solve(a, b):
    """
    :param a: A: matrix
    :param b: B: matrix (additional)
              C: vector location of columns
    :return:  X: vector of solutions
    """
    n = len(a)
    if isinstance(a, list) and isinstance(b, list) and n == len(b):
        for i in a:
            if len(i) != len(b):
                print("Incorrect data")
                return
    else:
        return

    c = matrix.create_vector(n)
    x = matrix.create_vector(n, 0)
    util.print_equation(a, b)

    for i in range(len(a) - 1):
        max_i, max_j = find_max_in_array(a, c, i)
        if max_i != max_j:
            # main element is not in main diagonal
            c[max_i], c[max_j] = c[max_j], c[max_i]

        if a[i][c[i]] != 0:
            m = a[i + 1][c[i]] / a[i][c[i]]
            matrix.mul_row(a, c, i, m)
            b[i] *= m
            for i2 in range(i + 1, len(a)):
                matrix.row_minus_row(a, c, i, i2)
                b[i2] -= b[i]
        util.print_equation_with_c(a, c, b)

    for i in range(len(a) - 1, 0, -1):
        if a[i][c[i]] != 0:
            m = a[i - 1][c[i]] / a[i][c[i]]
            print(f"m is {m}")
            matrix.mul_row(a, c, i, m)
            b[i] *= m
            util.print_equation_with_c(a, c, b)
            for i2 in range(i - 1, -1, -1):
                print("+ + + + +")
                matrix.row_minus_row(a, c, i, i2)
                b[i2] -= b[i]
            matrix.print_matrix_with_c(a, c)
        else:
            print(f"a[{i}][{c[i]}] == 0")
        util.print_equation_with_c(a, c, b)

    util.print_equation(a, b)

    is_number = 1
    for i in range(len(a)):
        solutions = list()
        solution_j = 0
        if is_number:
            for j in range(len(a)):
                if a[i][j] != 0:
                    solutions.append(a[i][j])
                    solution_j = j

            if len(solutions) > 1:
                print("Solution is not correct")
            else:
                x[solution_j] = b[i] / solutions[0]

        else:
            print("There is not solution")
    print(x)
    return x


solve([[20, 10], [17, 22]], [350, 500])
