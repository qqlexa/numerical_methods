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

    return x, iterations
