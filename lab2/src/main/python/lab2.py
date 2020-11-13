import math
from scipy.optimize import fsolve
import numpy as np
from colorama import Fore

from methods import util

from methods import gauss
from methods import cramer
from methods import inverse_matrix
from methods import iteration
from methods import seidel
from methods import newton


def read_maxtrix(file_name="INPUT.txt"):
    with open(file_name) as f:
        n = int(f.readline())
        array = list()
        for i in range(n):
            array.append([float(i) for i in f.readline().split()])
    return array, n


def read_vector(file_name="INPUT_A.txt"):
    with open(file_name) as f:
        n = int(f.readline())
        array = [float(i) for i in f.readline().split()]
    return array, n


def copy_matrix(b):
    return [[b[i][j] for j in range(len(b))] for i in range(len(b))]


def copy_vector(b):
    return [b[j] for j in range(len(b))]


"""
student_id = "12648067"
g = int(student_id[-1])  # 7
k = int(student_id[-2])  # 6

matrix = [[g + 1, g + 2, g + 3], [2 * (g + 1), g + 6, g - 5], [3 * (g + 1), g, -3]]
matrix_additional = [k, k + 1, k + 2]
"""

matrix, n = read_maxtrix()
matrix_additional, n = read_vector()
util.print_equation(matrix, matrix_additional)


def count_formula(z):
    return [matrix[0][0]*z[0] + matrix[0][1]*z[1] + matrix[0][2]*z[2] - matrix_additional[0],
            matrix[1][0]*z[0] + matrix[1][1]*z[1] + matrix[1][2]*z[2] - matrix_additional[1],
            matrix[2][0]*z[0] + matrix[2][1]*z[1] + matrix[2][2]*z[2] - matrix_additional[2]]


zGuess = np.array([0, 0, 0])
z = fsolve(count_formula, zGuess)
print(Fore.LIGHTCYAN_EX + f"{z}" + Fore.RESET)

print("1.")
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

print("2.")
eps = 0.0001
eq = [[24, 14, -8.1], [16, 26, 5.4], [8, 18, 27]]
eqAd = [8, 7, 6]
coefficient = [1, 2, 2.7]

x, iterations = iteration.solve(eq, eqAd, eps)
for i in range(len(x)):
    x[i] *= coefficient[i]

print(x)

print("3.")

student_id = "12648067"
g = int(student_id[-1])  # 7
k = int(student_id[-2])  # 6


def count_f1(args):
    return (28 + math.sin(7*args[0] + args[1] - 28) / 10) / 7


def count_f2(args):
    return math.sin(7*args[0] + args[1] - 28)/80


def f1(args):
    return (k+1)*args[0] - 4*g + math.sin((k+1)*args[0] + args[1] - 4*g)/10


def f2(args):
    return args[1] - math.sin((k+1)*args[0] + args[1] - 4*g)/(10*(g+1))


def dx_f1(args):
    return (k+1) + (k+1) * math.cos((k + 1)*args[0] + args[1] - 4*g)/10


def dy_f1(args):
    return math.cos((k + 1) * args[0] + args[1] - 4 * g)/10


def dx_f2(args):
    return - (k+1) * math.cos((k+1)*args[0] + args[1] - 4*g)/(10 * (g+1))


def dy_f2(args):
    return 1 - math.cos((k+1)*args[0] + args[1] - 4*g)/(10 * (g+1))


def count_formula(z):
    return [f1(z), f2(z)]


zGuess = np.array([0, 0])
z = fsolve(count_formula, zGuess)
print(Fore.LIGHTCYAN_EX + f"{z}" + Fore.RESET)

x, iterations = seidel.solve((count_f1, count_f2), eps=0.01, begin_positions=[0, 0])
print(f"Seidel's method: {x} in {iterations} iterations")


x, iterations = newton.solve([f1, f2],
                             [[dx_f1, dy_f1], [dx_f2, dy_f2]],
                             eps=0.01, begin_positions=[4.1, 0.2])

print(f"Newton's method: {x} in {iterations} iterations")
