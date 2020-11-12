import numpy as np
from methods import gauss
from methods import cramer
from methods import inverse_matrix
from methods import iteration
from methods import seidel


def read_maxtrix(file_name="INPUT.txt"):
    with open(file_name) as f:
        n = int(f.readline())
        array = list()
        for i in range(n):
            array.append([int(i) for i in f.readline().split()])

    return array, n


def read_vector(file_name="INPUT_A.txt"):
    with open(file_name) as f:
        n = int(f.readline())
        array = [int(i) for i in f.readline().split()]

    return array, n


def copy_matrix(b):
    a = list()
    for i in range(len(b)):
        c = list()
        for j in range(len(b)):
            c.append(b[i][j])
        a.append(c)
    return a


def copy_vector(b):
    a = list()
    for i in range(len(b)):
        a.append(b[i])
    return a


array, n = read_maxtrix()
array_additional, n = read_vector()

student_id = "12648067"
g = int(student_id[-1])  # 7
k = int(student_id[-2])  # 6

matrix = [[g + 1, g + 2, g + 3], [2 * (g + 1), g + 6, g - 5], [3 * (g + 1), g, -3]]
matrix_additional = [k, k + 1, k + 2]
print(matrix)

# print(X)
# [0.34294872 0.07692308 0.25641026]
eq = copy_matrix(matrix)
eqAd = copy_vector(matrix_additional)
x = cramer.solve(eq, eqAd)
print(x)

eq = copy_matrix(matrix)
eqAd = copy_vector(matrix_additional)
x = gauss.solve(eq, eqAd)
print(x)

eq = copy_matrix(matrix)
eqAd = copy_vector(matrix_additional)
x = inverse_matrix.solve(eq, eqAd)
print(x)

eps = 0.0001
eq = [[24, 14, -8.1], [16, 26, 5.4], [8, 18, 27]]
eqAd = [8, 7, 6]
coefficient = [1, 2, 2.7]

x, iterations = iteration.solve(eq, eqAd, eps)
for i in range(len(x)):
    x[i] *= coefficient[i]

print(x)


def count_f1(args):
    return (28 + math.sin(7*args[0] + args[1] - 28) / 10) / 7


def count_f2(args):
    return math.sin(7*args[0] + args[1] - 28)/80


solve((count_f1, count_f2), eps=0.01, begin_positions=[0, 0])
