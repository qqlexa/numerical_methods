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
    return c


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


def print_matrix_with_c(a, c):
    for i in range(len(a)):
        for j in range(len(a)):
            print(a[i][c[j]], end=" ")
        print()


def row_minus_row(a, c, i1, i2):
    if len(a) > i2:
        for j in range(len(a)):
            a[i2][c[j]] -= a[i1][c[j]]
    else:
        print("Array border")


def mul_row(a, c, i, number):
    for j in range(len(a)):
        a[i][c[j]] *= number

