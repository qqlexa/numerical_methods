def print_equation(a, b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print(b[i])
    print()


def create_matrix(n):
    c = list()
    for _ in range(n):
        x = list()
        for j in range(n):
            x.append(j)
        c.append(x)
    return c
