def print_equation(a, b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print(b[i])
    print()


def print_equation_with_c(a, c, b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][c[j]], end=" ")
        print(b[i])
    print()

