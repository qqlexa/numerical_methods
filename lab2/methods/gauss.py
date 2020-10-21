# Gauss matrix method

def solve(a, b):
    # A - matrix
    # B -
    # X - array of solutions
    x = list()
    for i, j in zip(a, b):
        for i2 in i:
            print(i2, end=" ")
        print(j)

    return x


solve([[4, 5], [4, 6]], [2, 3])
