# Gauss matrix method
import util


def find_max_in_array(a, line=-1):
    """
    :param a: matrix
    :param line: line of finding, if -1 find all matrix
    :return: tuple (i, j)
    """
    if line < 0:
        max_number = a[0][0]
        max_i = 0
        max_j = 0
        for i in range(len(a)):
            for j in range(len(a)):
                if max_number < a[i][j]:
                    max_number = a[i][j]
                    max_i = i
                    max_j = j

    else:
        max_number = a[line][0]
        max_i = line
        max_j = 0
        for j in range(len(a)):
            if max_number < a[line][j]:
                max_number = a[line][j]
                max_j = j
    return max_i, max_j


def solve(a, b):
    """
    :param a: A: matrix
    :param b: B: matrix (additional)
              C: location rows
    :return:  X: solutions
    """
    n = len(a)
    if isinstance(a, list) and isinstance(b, list) and n == len(b):
        for i in a:
            if len(i) != len(b):
                print("Incorrect data")
                return
    else:
        return

    c = util.create_matrix(n)

    x = list()
    util.print_equation(a, b)

    pos = find_max_in_array(a, 0)
    if pos[0] != pos[1]:
        # main element is not in main diagonal
        j1 = pos[1]
        if pos[]
        if n > pos[1] + 1:
            j2 = pos[1] + 1
        else:
            j2 = pos[1] - 1
        for i in range(n):
            if n > pos[1] + 1:
                a[pos[0]][pos[1]], a[pos[0]][pos[1] + 1] = a[pos[0]][pos[1] + 1], a[pos[0]][pos[1]]
            else:
    print(pos)
    print(a[pos[0]][pos[1]])

    util.print_equation(a, b)

    return x


solve([[4, 5], [4, 6]], [2, 3])
