def create_vector(n, number=-1):
    c = list()
    for i in range(n):
        if number < 0:
            c.append(i)
        else:
            c.append(number)
    return c


def print_vector(c):
    for i in c:
        print(i, end=" ")
    print()


def create_matrix(n):
    c = list()
    for _ in range(n):
        x = list()
        for j in range(n):
            x.append(j)
        c.append(x)
    return c


def print_matrix(a):
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][j], end=" ")
        print()


def row_minus_row(a, from_i, minus_i):
    if len(a) > from_i and len(a) > minus_i:
        for j in range(len(a)):
            a[from_i][j] -= a[minus_i][j]
    else:
        print("Array border")


def mul_row(a, i, number):
    for j in range(len(a)):
        a[i][j] *= number

