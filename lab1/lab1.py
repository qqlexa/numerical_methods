# https://www.wolframalpha.com/input/?i=%28x+-+42%29+%5E+2+%2B+sin%28x+-+42%29

from sympy import sin
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import fsolve
from colorama import Fore


def count_f1(x):
    return (x - g * k) ** 2 + math.sin(x - g * k)


def d_f1(x):
    return 2*x + math.cos(x - 42) - 84


def dd_f1(x):
    return 2 - math.sin(x - 42)


def count_phi2(x):
    """
    (kx - 10g) - sin(x - 10g/k) = 0
    kx = sin(x - 10g/k) + 10g
    x = (sin(x - 10g/k) + 10g)/k
    """
    return (math.sin(x - 10 * g / k) + 10 * g) / k


def create_plot(x, y, parameters):
    """

    :param x: argument
    :param y: function
    :param parameters: list from [dict(), dict(), dict() .. . . . .]
    dict:
        "color"
        "description"
        "solution"
    :return:
    """
    # setting the axes at the centre
    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')  # left border
    ax.spines['bottom'].set_position('zero')  # bottom border
    ax.spines['right'].set_color('none')     # right border
    ax.spines['top'].set_color('none')         # top border
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    for i in parameters:
        plt.plot(x, y, i["color"], label="{method} {solution}".format(method=i["description"], solution=i["solution"]))

    # show the plot
    plt.legend(loc="upper left")
    plt.title("lab1 | qqlexa")
    plt.show()


def find_result_by_half(a, b, d, eps, f):
    solutions = []
    for i in ((a, b), (b, d)):
        a = i[0]
        b = i[1]
        while b - a > eps:
            c = (b + a) / 2

            if abs(f(c)) <= eps ** 2:
                break

            elif f(a) * f(c) < 0:
                # [a, c]
                b = c

            elif f(c) * f(b) < 0:
                # [c, b]
                a = c
            else:
                print("solution is not found")
                break

        solutions.append((b + a) / 2)

    return solutions


def find_result_by_chord(a, b, d, eps, f):
    solutions = []
    for i in ((a, b), (b, d)):

        a = i[0]
        b = i[1]
        x_t = a - ((f(a) * (b - a)) / (f(b) - f(a)))
        x_p = a
        while abs(x_t - x_p) > eps:
            if abs(f(x_t)) <= eps ** 2:
                break
            elif f(a) * f(x_t) < 0:
                b = x_t
            elif f(x_t) * f(b) < 0:
                a = x_t
            else:
                print("solutions not found")
                break
            x_p = x_t
            x_t = a - ((f(a) * (b - a)) / (f(b) - f(a)))
        solutions.append(x_t)

    return solutions


def find_result_by_tangent(a, b, d, eps, f, f_d, f_dd):
    solutions = []
    for i in ((a, b), (b, d)):
        a = i[0]
        b = i[1]

        if f(a) * f_dd(a) > 0:
            x_t = a
        else:
            # f(b) * f_dd(b) > 0
            x_t = b

        x_p = b if x_t == a else a

        while abs(x_t - x_p) > eps:
            x_p = x_t
            x_t = x_p - f(x_p) / f_d(x_p)

        solutions.append(x_t)

    return solutions


def find_result_by_iterations(a, b, eps, f):
    solutions = []
    x_p = (a + b) / 2
    x_t = f(x_p)
    while abs(x_t - x_p) > eps:
        x_p = x_t
        x_t = f(x_p)

    solutions.append(x_t)

    return solutions


def main():
    global g, k
    eps = 0.01
    student_id = "12648067"
    g = int(student_id[-1])  # 7
    k = int(student_id[-2])  # 6

    a = 40.0
    b = 41.7
    d = 42.5

    print("g = {g} | k = {k} ".format(g=g, k=k))

    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fsolve.html#:~:text=Find%20the%20roots%20of%20a,0%20given%20a%20starting%20estimate.&text=A%20function%20that%20takes%20at,value%20of%20the%20same%20length

    def func(m):
        return (m - g * k) ** 2 + np.sin(m - g * k)

    def func2(m):
        return (k * m - 10 * g) - np.sin(m - 10 * g / k)

    root = fsolve(func, [a, d])
    print("(x - {g} * {k}) ** 2 + sin(x - {g} * {k})".format(g=g, k=k))
    print("The right solve:" + Fore.GREEN)
    print(root)

    # half-method
    print(Fore.RESET + "half-method solutions")
    print(find_result_by_half(a, b, d, eps, count_f1))

    # chord-method
    print("chord-method solutions")
    print(find_result_by_chord(a, b, d, eps, count_f1))

    # tangent-method
    print("tangent-method solutions")
    print(find_result_by_tangent(a, b, d, eps, count_f1, d_f1, dd_f1))

    # draw plot
    x = np.linspace(-500, 500, 1000000)

    y = (x - g * k) ** 2 + np.sin(x - g * k)

    create_plot(x, y, [{"color": "r", "description": "Half: ",
                        "solution": find_result_by_half(a, b, d, eps, count_f1)},
                       {"color": "g", "description": "Chord: ",
                        "solution": find_result_by_chord(a, b, d, eps, count_f1)},
                       {"color": "b", "description": "Tangent: ",
                        "solution": find_result_by_tangent(a, b, d, eps, count_f1, d_f1, dd_f1)}])

    print()
    print()
    
    y = (k * x - 10 * g) - np.sin(x - 10 * g / k)

    a = 11.5
    b = 11.7

    root = fsolve(func2, [a, b])
    print("({k} * x - 10 * {g}) - sin(x - 10 * {g} / {k})".format(g=g, k=k))
    print("The right solve:" + Fore.GREEN)
    print(root)

    # iterations-method
    print(Fore.RESET + "iterations-method solution")
    print(find_result_by_iterations(a, b, eps, count_phi2))

    create_plot(x, y, [{"color": "b", "description": "Iterations: ",
                       "solution": find_result_by_iterations(a, b, eps, count_phi2)}])


if __name__ == '__main__':
    main()

# Висновок, що якщо взяти великий відрізок - точність досягається шляхом лініїзації дуже швидко
