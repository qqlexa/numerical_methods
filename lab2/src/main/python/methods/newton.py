# Newton method
import math

try:
    import util
    import matrix
    import cramer
except:
    try:
        from . import util
        from . import matrix
        from . import cramer
    except:
        pass


def norm(x):
    return math.sqrt(sum([_x**2 for _x in x]))


def solve(functions, derivative_functions, eps=0.01, begin_positions=()):
    iterations = 1
    n = len(functions)

    x = [0 for i in range(n)]
    if len(begin_positions) == 0:
        begin_positions = [0 for i in range(n)]
    xk = [i for i in begin_positions]

    while abs(norm(x) - norm(xk)) > eps:
        x = [i for i in xk]

        a = [[derivative_functions[i][j](x) for j in range(n)] for i in range(n)]
        b = [-f(x) for f in functions]

        p = cramer.solve(a, b)
        xk = [x[i] + p[i] for i in range(n)]

        iterations += 1

    print(x)
    print(iterations)
    return x, iterations


student_id = "12648067"
# g = int(student_id[-1])  # 7
# k = int(student_id[-2])  # 6
k = 7
g = 9


def f1(x):
    return (k+1)*x[0] - 4*g + math.sin((k+1)*x[0] + x[1] - 4*g)/10


def f2(x):
    return x[1] - math.sin((k+1)*x[0] + x[1] - 4*g)/(10*(g+1))


def dx_f1(x):
    return (k+1) + (k+1) * math.cos((k + 1)*x[0] + x[1] - 4*g)/10


def dy_f1(x):
    # dz/dy:  (cos((k + 1)*x + y - 4*g)/10)/10
    return math.cos((k + 1) * x[0] + x[1] - 4 * g)/10


def dx_f2(x):
    return - (k+1) * math.cos((k+1)*x[0] + x[1] - 4*g)/(10 * (g+1))


def dy_f2(x):
    return 1 - math.cos((k+1)*x[0] + x[1] - 4*g)/(10 * (g+1))

"""

# Похідна першої функції по x
# k = 7
# k = 7


def df1_dx(x):
    return 8 + (4 * math.cos(8 * x[0] + x[1] - 36)) / 5


# Похідна першої функції по y
def df1_dy(x):
    return math.cos(8 * x[0] + x[1] - 36) / 10


# Похідна другої функції по х
def df2_dx(x):
    return -(2 * math.cos(8 * x[0] + x[1] - 36)) / 25


# Похідна другої функції по y
def df2_dy(x):
    return -(math.cos(8 * x[0] + x[1] - 36)) / 100 + 1
"""


solve([f1, f2], [[dx_f1, dy_f1], [dx_f2, dy_f2]], eps=0.01, begin_positions=[1, 1])
