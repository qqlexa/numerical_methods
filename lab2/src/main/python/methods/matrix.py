def create_vector(n, number=-1):
    c = list()
    for i in range(n):
        if number < 0:
            c.append(i)
        else:
            c.append(number)
    return c


def is_square_matrix(a):
    if not isinstance(a, list) and not isinstance(a, tuple):
        print("Error. Matrix is not list() or tuple()")
        return False

    if len(a) == 0:
        print("Error. Matrix is clear")
        return False

    if not isinstance(a[0], list) and not isinstance(a, tuple):
        print("Error. Matrix[0] is not list() or tuple()")
        return False

    return len(a) == len(a[0])


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


def cut_row_and_column(a, _i, _j):
    matrix = list()
    for i in range(len(a)):
        row = list()
        if _i == i:
            continue
        for j in range(len(a)):
            if _j == j:
                continue
            row.append(a[i][j])
        matrix.append(row)
    return matrix


def find_union_matrix(a):
    if find_det(a) == 0:
        print("It is not possible to find union matrix. Determinant equals 0")
        return False

    b = create_matrix(len(a))
    for i in range(len(a)):
        for j in range(len(a)):
            sign = -1 if (i + j) % 2 else 1
            b[i][j] = sign * find_det(cut_row_and_column(a, i, j))

    return b


def transpose_matrix(a):
    b = create_matrix(len(a))
    for i in range(len(a)):
        for j in range(len(a)):
            b[i][j] = a[j][i]

    return b


def find_det(a):
    if not is_square_matrix(a):
        print("It is not possible to find determinant")
        return False

    if len(a) == 1:
        result = a[0][0]
    elif len(a) == 2:
        result = a[0][0]*a[1][1] - a[0][1]*a[1][0]
    else:
        result = 0
        for i in range(len(a)):
            sign = -1 if i % 2 else 1
            result += sign * a[i][0] * find_det(cut_row_and_column(a, i, 0))
    # print(f"result {result}")
    return result
