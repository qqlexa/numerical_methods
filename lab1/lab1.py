"""
https://www.wolframalpha.com/input/?i=%28x+-+42%29+%5E+2+%2B+sin%28x+-+42%29

Лабораторна робота 1

Тема: Чисельне розв’язання нелінійних рівнянь
Дисципліна: ЧИСЕЛЬНІ МЕТОДИ

- Розробити алгоритми та програмне забезпечення для розв’язку наведеної задачі вказаними методами.
- Алгоритми представити у вигляді блок-схем або діаграм діяльності UML.
+ Програмне забезпечення розробити на будь-якій сучасній мові програмування.
- Відділеня коренів здійснити побудовою графіків функції з використанням математичних пакетів.
- Абсолютна похибка має дорівнювати 0,01.
- Знайти точне значення розв’язку задачі за допомогою математичних бібліотек та порівняти його зі значенням, отриманим
у результаті роботи розробленого програмного забезпечення.

+ 1.Знайти розв’язок рівняння  f(x) = (x - g * k)^2 + sin(x- g * k) = 0
(де g – остання цифра у номері студентського квитка, а k – передостання)
методами ділення +навпіл+, +хорд+ та +дотичних+ (Ньютона).

2.Знайти розв’язок рівняння f(x) = (k * x - 10g) - sin(x - 10g / k) = 0
(де g – остання цифра у номері студентського квитка, а k – передостання)
методом ітерацій. < < < < <


Звіт з завдання має містити:
1.	Титульний аркуш.
2.	Завдання відповідно до варіанту.
3.	Опис розв’язку задачі (математичну постановку, алгоритми, лістинг програми, результати її роботи,
пошук точного рішення, висновки на основі порівняння точного розв’язку та знайденого за допомогою розробленої програми).
Захист звіту передбачає також опитування з теоретичних питань щодо застосованих методів та засобів.
Максимальна оцінка за роботу – 10 балів.
При несвоєчасному захисті звіту штраф 5 балів.

"""
from sympy import symbols, sin, diff, solve
import matplotlib.pyplot as plt
import numpy as np
import math


def find_diff():
    x = symbols("x")
    eq_1 = diff((k * x - 10 * g) - sin(x - 10 * g / k))
    eq_2 = diff(diff((k * x - 10 * g) - sin(x - 10 * g / k)))

    print(eq_1)
    print(eq_2)

    print(eq_1.subs(x, 42))
    print(eq_2.subs(x, 42))


def count_f1(x):
    return (x - g * k) ** 2 + math.sin(x - g * k)


def d_f1(x):
    return 2*x + math.cos(x - 42) - 84


def dd_f1(x):
    return 2 - sin(x - 42)


def count_f2(x):
    return (k * x - 10 * g) - math.sin(x - 10 * g / k)


def d_f2(x):
    return 6 - math.cos(x - 11.6666666666667)


def dd_f2(x):
    return math.sin(x - 11.6666666666667)


def create_plot(x, y):
    print("Plot")
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
    for i in y:
        plt.plot(x, i[0], i[1], label=i[2])
        for j in i[3]:
            plt.plot(x, i[0], i[1], label="Solution: %s " % j)

    # show the plot
    plt.legend(loc="upper left")
    plt.title("lab1 | qqlexa")
    plt.show()


def find_result_by_half(a, b, d, eps, f):
    solution = []
    for i in ((a, b), (b, d)):
        a = i[0]
        b = i[1]
        if f(a) * f(b) < 0:

            while b - a > eps:
                c = (b + a) / 2

                if 0 <= abs(f(c)) <= eps:
                    break

                elif f(a) * f(c) < 0:
                    # [a, c]
                    b = c

                elif f(c) * f(b) < 0:
                    # [c, b]
                    a = c
                else:
                    print("Solution is not found")

            solution.append((b + a) / 2)

    return solution


def find_result_by_chord(a, b, d, eps, f):
    solution = []
    for i in ((a, b), (b, d)):

        a = i[0]
        b = i[1]
        if f(a) * f(b) < 0:
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
                    print("Solution not found")
                    break
                x_p = x_t
                x_t = a - ((f(a) * (b - a)) / (f(b) - f(a)))
            solution.append(x_t)

    return solution


def find_result_by_tangent(a, b, d, eps, f, f_d, f_dd):
    solution = []
    for i in ((a, b), (b, d)):
        a = i[0]
        b = i[1]

        if f(a) * f_dd(a) > 0:
            x_t = a
        else:
            # f(b) * f_dd(b) > 0
            x_t = b

        x_p = eps * 2

        while abs(x_t - x_p) > eps:
            x_p = x_t
            x_t = x_p - f(x_p) / f_d(x_p)

        solution.append(x_t)

    return solution


def main():
    global k, g
    eps = 0.01
    student_id = "12648067"
    g = int(student_id[-1])  # 7
    k = int(student_id[-2])  # 6

    a = 40
    b = 41.7
    d = 42.5

    print("g = {g} | k = {k} ".format(g=g, k=k))

    # half-method
    print(find_result_by_half(a, b, d, eps, count_f1))
    # print(find_result_by_half(a, b, d, eps, count_f2))

    # chord-method
    print("chord-method")
    print(find_result_by_chord(a, b, d, eps, count_f1))
    # print(find_result_by_chord(a, b, d, eps, count_f2))

    print()
    print("tangent-method")
    # tangent-method
    print(find_result_by_tangent(a, b, d, eps, count_f1, d_f1, dd_f1))
    # print(find_result_by_tangent(a, b, d, eps, count_f2, d_f2, dd_f2))

    # draw plot
    x = np.linspace(-500, 500, 1000000)

    y1 = (x - g * k) ** 2 + np.sin(x - g * k)
    # y2 = (k * x - 10 * g) - np.sin(x - 10 * g / k)
    create_plot(x, [[y1, "r", "(x - {g} * {k}) ** 2 + sin(x - {g} * {k})".format(k=k, g=g),
                     find_result_by_half(a, b, d, eps, count_f1)],
                    [y1, "g", "(x - {g} * {k}) ** 2 + sin(x - {g} * {k})".format(k=k, g=g),
                     find_result_by_chord(a, b, d, eps, count_f1)],
                    [y1, "b", "(x - {g} * {k}) ** 2 + sin(x - {g} * {k})".format(k=k, g=g),
                     find_result_by_tangent(a, b, d, eps, count_f1, d_f1, dd_f1)]])


if __name__ == '__main__':
    main()

# Висновок, що якщо взяти великий відрізок - точність досягається шляхом лініїзації дуже швидко
