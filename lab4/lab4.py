def primitive_func(a: float, b: float):
    # x**3 + x
    # primitive = (x**4)/4 + (x**2)/2
    return ((b**4 - a**4) / 4) + ((b**2 - a**2) / 2)


def func_d(x: float):
    # x**3 + x
    return 3 * x**2 + 1


def func(x: float):
    return x**3 + x


def get_increase(x, eps=0.0001):
    k = 1
    h = 0.5 / 5 ** (k - 1)
    d_currently = (func(x+h) - func(x))/h
    d_previously = d_currently + 2 * eps
    while abs(d_previously - d_currently) > eps:
        k += 1
        d_previously = d_currently

        h = 0.5 / 5 ** (k - 1)
        d_currently = (func(x + h) - func(x)) / h
    print(f"Похибка між знайденим і точним значеннями: {func_d(x) - d_currently}")
    print(f"Кількість ітерацій: {k}")
    return d_currently


def get_center_difference(x: float, eps=0.01):
    k = 1
    h = 0.5**k
    d_currently = (func(x + h) - func(x - h)) / (2 * h)

    k += 1
    h = 0.5**k
    d_next = (func(x + h) - func(x - h)) / (2 * h)

    k += 1
    h = 0.5**k
    d_previously, d_currently, d_next = d_currently, d_next, (func(x + h) - func(x - h)) / (2 * h)

    while abs(d_next - d_currently) < abs(d_currently - d_previously) and abs(d_next - d_currently) > eps:
        k += 1
        h = 0.5 ** k
        d_previously, d_currently, d_next = d_currently, d_next, (func(x + h) - func(x - h)) / (2 * h)

    print(f"Похибка між знайденим і точним значеннями: {abs(func_d(x) - d_currently)}")
    print(f"Кількість ітерацій: {k}")
    return d_currently


def get_square_interpolation(x: float, list_x: list):
    list_y = [func(i) for i in list_x]
    delta_y0 = list_y[1] - list_y[0]
    delta_y1 = list_y[2] - list_y[1]
    delta_y02 = delta_y1 - delta_y0

    h = abs(list_x[0] - list_x[1])
    q = (x - list_x[0]) / h
    result = (delta_y0 + (2 * q - 1) / 2 * delta_y02) / h
    print(f"Точне значення: {func_d(x)}")
    print(f"Похибка між знайденим і точним значеннями: {abs(func_d(x) - result)}")
    return result


def get_left_rectangles(a: float, b: float, n: int):
    h = (b-a)/n
    _sum = 0
    for i in range(n):
        _sum += func(a + i*h)
    result = h * _sum

    exactly = primitive_func(a, b)
    print(f"Кількість ітерацій: {n}")
    print(f"Точне значення: {exactly}")
    print(f"Похибка між знайденим і точним значеннями: {abs(exactly - result)}")
    return result


def get_trapeze(a: float, b: float, n: int):
    h = (b - a) / n

    _sum = 0
    #              Точка n береться невключно, тому й [1; n) теж саме що і [1; n-1]
    for i in range(1, n):
        _sum += func(a + i*h)
    result = h * ((func(a) + func(b)) / 2 + _sum)

    exactly = primitive_func(a, b)
    print(f"Кількість ітерацій: {n}")
    print(f"Точне значення: {exactly}")
    print(f"Похибка між знайденим і точним значеннями: {abs(exactly - result)}")
    return result


def get_simpson(a: float, b: float, m: int):
    n = 2*m
    h = (b - a) / n

    y = [func(a + i*h) for i in range(n+1)]
    _sum = 0
    #              Точка n береться невключно, тому й [1; m+1) теж саме що і [1; m]
    for i in range(1, m+1):
        _sum += y[2*i - 2] + 4*y[2*i - 1] + y[2*i]
    result = h/3 * _sum

    exactly = primitive_func(a, b)
    print(f"Кількість ітерацій: {n}")
    print(f"Точне значення: {exactly}")
    print(f"Похибка між знайденим і точним значеннями: {abs(exactly - result)}")
    return result


student_id = "12648067"
g = int(student_id[-1])  # 7
k = int(student_id[-2])  # 6

vector_x = [g - 2*k - 3, g - 2*k - 1.5, g - 2*k]

x = g - 2*k - 2
a = g-2*k-3
b = g-2*k
n = 1000

print(f"Вибраний x: {x}")
print(f"Правильне значення похідної у цій точці: {func_d(x)}")
print()

print("1.")
print("Послідовність відношень приростів")
print(get_increase(x))
print()

print("Центрована різниця (порядку точності 2)")
print(get_center_difference(x))
print()

print("2.")
print("Квадратична інтерполяція")
print(get_square_interpolation(x, vector_x))
print()

print("3.")
print(f"Межі інтеграла a={a}, b={b}")

print("Лівих прямокутників")
print(get_left_rectangles(a, b, n))
print()

print("Трапецій")
print(get_trapeze(a, b, 20))
print()

print("Сімпсона")
print(get_simpson(a, b, 1))
print()

