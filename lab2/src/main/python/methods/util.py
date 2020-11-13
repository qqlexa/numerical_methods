def print_equation(a, b):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print(f"| {b[i]}")
    print()
