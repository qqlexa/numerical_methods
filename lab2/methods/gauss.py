# Gauss matrix method

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
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print(b[i])

    return x


solve([[4, 5], [4, 6]], [2, 3])
