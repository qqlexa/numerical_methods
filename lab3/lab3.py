import math
import numpy as np
import matplotlib.pyplot as plt

import matrix


def create_plot(x, y, x2 : list, y2: list):
    """
    :param x: argument
    :param y: function
    :param x2: points x2
    :param x2: points y2
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
    plt.plot(x, y)
    for i in range(len(x2)):
        plt.scatter(x2[i], y2[i], s=50)

    # show the plot
    plt.legend(loc="upper left")
    plt.title("lab3 | qqlexa")
    plt.show()


def count_func(x):
    return math.sin(x) + x


def count_lagrange(x, _x, _y):
    result = list()
    for i in range(len(x)):
        _sum = 0
        for j in range(len(_x)):
            mul = 1
            for p in range(len(_x)):
                if p != j:
                    mul *= (x[i] - _x[p]) / (_x[j] - _x[p])
            _sum += _y[j] * mul
        result.append(_sum)

    return result


def dy(y, x):
    if len(y) > 2:
        y_left = [i for i in y]
        x_left = [i for i in x]
        x_left.pop(0)
        y_left.pop(0)
        y_right = [i for i in y]
        x_right = [i for i in x]
        x_right.pop()
        y_right.pop()
        return (dy(y_left, x_left) - dy(y_right, x_right)) / (x[-1] - x[0])
    elif len(y) == 2:
        return (y[1] - y[0]) / (x[1] - x[0])
    return 0


def count_newton(x, _x, _y):
    result = list()
    for x_element in x:
        res = _y[0]
        for i in range(1, len(_y)):
            x_list = list()
            y_list = list()
            buf = 1
            for j in range(i + 1):
                x_list.append(_x[j])
                y_list.append(_y[j])
                if j < i:
                    buf *= x_element - _x[j]

            res += dy(y_list, x_list) * buf
        result.append(res)
    return result


def dy_step(y, x, number, index):
    if number > 1:
        return dy_step(y, x, number-1, index+1) - dy_step(y, x, number-1, index)
    elif number == 1:
        return y[index+1] - y[index]
    return 0


def count_newton_step(x, _x, _y, h):
    result = list()
    for x_element in x:
        res = _y[0]

        x_list = [i for i in _x]
        y_list = [i for i in _y]

        q = (x_element - _x[0]) / h
        buf = 1
        for i in range(1, len(_y)):
            buf *= (q - i + 1) / i
            res += dy_step(y_list, x_list, i, 0) * buf
        result.append(res)
    return result


def count_chebishev_point(left: float, right: float, p: float):
    t = math.cos(((2 * p + 1) * math.pi) / 8)
    return (left + right) / 2 + ((right - left) * t) / 2


def count_chebishev(x, interval):
    _x = list()
    _y = list()

    for i in range(len(x) + 1):
        _x.append(count_chebishev_point(interval[0], interval[1], i))  # g -2k-3, g-2k+2
        _y.append(count_func(_x[i]))
    # _x - array new dots
    return count_lagrange(x, _x, _y)


def count_spline(x, _x, _y):
    a = list()
    b = list()
    result = list()
    for i in range(len(_x) - 1):
        a.append((_y[i] - _y[i + 1]) / (_x[i] - _x[i + 1]))
        b.append(_y[i] - (a[i] * _x[i]))

    for i in range(len(_x) - 1):
        for j in range(len(_x) - 1):
            if _x[j] <= x[i] <= _x[j + 1]:
                result.append(a[i] * x[i] + b[i])
                break
    return result


def count_linear_func(a, b, x):
    return a + b*x


def count_small_square(x, _x, _y):
    """print("PRSS")
    u = [[1 if j == 0 else _x[i] for j in range(2)] for i in range(len(_x))]
    # b = [ut * u]-1 * ut * y
    print(u)
    b = [[u[i][j] for j in range(len(u[i]))] for i in range(len(u))]
    print(b)
    ut = newton.transpose_matrix(u)
    print(ut)

    b = newton.mul_matrix(ut, u)
    print(b)
    b = newton.get_inverse_matrix(b)
    print(b)
    b = newton.mul_matrix(b, ut)
    print(b)
    new_y = [[c_y for _ in range(1)] for c_y in _y]
    print(new_y)
    print("New")
    b = newton.mul_matrix(b, new_y)
    print(b)
    """
    x_x = [i*i for i in _x]
    x_y = [i*j for i, j in zip(_x, _y)]
    arr = [[j for j in range(2)] for _ in range(2)]
    arr_y = [i for i in range(2)]

    arr[0][0] = sum(x_x)
    arr[0][1] = sum(_x)
    arr[1][0] = int(arr[0][1])
    arr[1][1] = len(_x)
    arr_y[0] = sum(x_y)
    arr_y[1] = sum(_y)

    t_arr = matrix.get_inverse_matrix(arr)
    a = t_arr[1][0] * arr_y[0] + t_arr[1][1] * arr_y[1]
    b = t_arr[0][0] * arr_y[0] + t_arr[0][1] * arr_y[1]

    print(f"y = {a} + {b}x")

    result = [count_linear_func(a, b, i) for i in x]
    return result, a, b

"""
student_id = "12648067"
g = int(student_id[-1])  # 7
k = int(student_id[-2])  # 6
"""

"""
1. f(x) = sin(x) + x
table 1.
x     g-2k-3 | g-2k-1 | g-2k | g-2k + 2
f(x)  _______|________|______|__________
в точках x = [g-2k-2.7, g-2k-0.5, g-2k+2.8]

2. Чебишев
відрізок = [g-2k-3, g-2k+2]
нова таблиця f(x)
порівняти лагранжа 1 і в 2 в точках x = [g-2k-2.7, g-2k-0.5, g-2k+2.8]

3. f(x) = sin(x) + x
table 2.
x     g-2k-3 | g-2k-1 | g-2k | g-2k + 1
f(x)  _______|________|______|__________

в точках x = [g-2k-1.7, g-2k-0.5, g-2k+1.8]

4. Сплайн
в точках x = [g-2k-1.7, g-2k-0.5, g-2k+0.8]

5. y = a + bx
в точках x = [g-2k-2.7, g-2k-0.5, g-2k+2.8]
порівняти з #3

"""


def print_delta(x, exactly_y, inexactly_y, info=""):
    print(info)
    for i in range(len(result)):
        print(f"{x[i]}: {inexactly_y[i]}  func: {exactly_y[i]}    delta: {abs(inexactly_y[i] - exactly_y[i])}")


def print_info(info_x, info_y, info):
    print(info)
    print("x    | ", end="")
    for i in range(len(info_x)):
        print(f"{info_x[i]:12d}", end="")
    print()

    print("f(x) | ", end="")
    for i in range(len(info_y)):
        print(f"{round(info_y[i], 5):12f}", end="")
    print()

"""
my_x = [g-2*k-3, g-2*k-1, g-2*k, g-2*k + 2]  # [-11, -9, -8, -6]
my_y = [count_func(i) for i in my_x]

my_x2 = [g-2*k-3, g-2*k-1, g-2*k, g-2*k + 1]  # [-10, -9, -8, -7]
my_y2 = [count_func(i) for i in my_x2]

cur_x = [g-2*k-2.7, g-2*k-0.5, g-2*k+2.8]  # [-10.7, -8.5, -5.2]
cur_y = [count_func(i) for i in cur_x]

cur_x2 = [g-2*k-1.7, g-2*k-0.5, g-2*k+1.8]  # [-9.7, -8.5, -6.2]
cur_y2 = [count_func(i) for i in cur_x2]

cur_x3 = [g-2*k-1.7, g-2*k-0.5, g-2*k+0.8]  # [-9.7, -8.5, -7.2]
cur_y3 = [count_func(i) for i in cur_x3]


print_info(my_x, my_y, info="Table 1")
print_info(my_x2, my_y2, info="Table 2")

result = count_lagrange(cur_x, my_x, my_y)
print_delta(cur_x, cur_y, result, "Lagrange method:")

result = count_newton(cur_x, my_x, my_y)
print_delta(cur_x, cur_y, result, "Newton method:")

result = count_newton_step(cur_x2, my_x2, my_y2, 1)
print_delta(cur_x2, cur_y2, result, "Newton method with step:")

result = count_chebishev(cur_x, [g-2*k-3, g-2*k+2])
print_delta(cur_x, cur_y, result, "Chebishev method:")

result = count_spline(cur_x3, my_x, my_y)
print_delta(cur_x2, cur_y2, result, "Spline method:")

print("Square method:")
result, a, b = count_small_square(cur_x2, my_x2, my_y2)
print_delta(cur_x2, cur_y2, result)
#  plot_x = np.array(x)
plot_x = np.linspace(-10, 2, 1000000)

plot_y = a + b * plot_x
create_plot(plot_x, plot_y, my_x2, my_y2)
"""
def count_func(x):
	return math.exp(x)*math.sin(x)
	
cur_x = list(range(7))
my_x = [0, 6]  # [-11, -9, -8, -6]
my_y = [count_func(i) for i in my_x]
result = count_lagrange(cur_x, my_x, my_y)
print(result)

