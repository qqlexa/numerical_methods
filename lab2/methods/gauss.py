# Gauss matrix method

def print_equation(a, b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print(b[i])
    print()


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
    :return:  X: solutions
    """
    if isinstance(a, list) and isinstance(b, list):
        for i in a:
            if len(i) != len(b):
                print("Incorrect data")
                return

    x = list()
    print_equation(a, b)

    pos = find_max_in_array(a, 0)
    print(pos)
    print(a[pos[0]][pos[1]])

    print_equation(a, b)

    return x


solve([[4, 5], [4, 6]], [2, 3])
