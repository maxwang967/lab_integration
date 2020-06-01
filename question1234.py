# -*- coding: utf-8 -*-
# @Time    : 2020/6/1 12:00 上午
# @Author  : morningstarwang
# @FileName: question1234.py
# @Blog: wangchenxing.com
from datetime import datetime
from math import pi, sin, cos, e, sqrt

ERROR = 1e-7


def get_s(t1, t2):
    return (1 / 3) * (4 * t2 - t1)


def get_c(s1, s2):
    return (1 / 15) * (16 * s2 - s1)


def get_r(c1, c2):
    return (1 / 63) * (64 * c2 - c1)


def get_w(r1, r2):
    return (1 / 255) * (256 * r2 - r1)


def gauss_ch2(f, n):
    sigma = 0.0
    for k in range(n):
        sigma += (sin(k * pi / (n + 1)) ** 2) * f(cos((k * pi) / n + 1))
    return (pi / (n + 1)) * sigma


def comp_gauss_leg(f, a, b):
    k = 1
    T = [0 for _ in range(1000)]
    while True:
        h = (b - a) / (2 ** (k - 1))
        for j in range(int(2 ** (k - 1))):
            x_j = a + j * h
            x_j1 = x_j + h
            T[k] += gauss_leg(f, x_j, x_j1)
        if abs(T[k] - T[k - 1] < ERROR):
            break
        k += 1
    return T[k]


def gauss_leg(f, a, b):
    return (b - a) / 2 * (f(((a-b) / (2 * sqrt(3))) + ((a + b) / 2)) + f(((b - a) / (2 * sqrt(3))) + ((a + b) / 2)))


def comp_trep(f, a, b):
    k = 0
    T = [0 for _ in range(1000)]
    while True:
        if k == 0:
            T[k] = ((b - a) / 2) * (f(a) + f(b))
        else:
            h = (b - a) / (2 ** (k - 1))
            sigma = 0.0
            for i in range(int(2 ** (k - 1))):
                sigma += f(a + i * h + 0.5 * h)
            T[k] = 0.5 * T[k - 1] + 0.5 * h * sigma
        if k - 1 >= 0 and abs(T[k] - T[k - 1]) < ERROR:
            break
        k += 1
    return T[k]


def romberg(f, a, b):
    k = 0
    T = [0 for _ in range(5)]
    while k < 5:
        if k == 0:
            T[k] = ((b - a) / 2) * (f(a) + f(b))
        else:
            h = (b - a) / (2 ** (k - 1))
            sigma = 0.0
            for i in range(int(2 ** (k - 1))):
                sigma += f(a + i * h + 0.5 * h)
            T[k] = 0.5 * T[k - 1] + 0.5 * h * sigma
        k += 1
    print(T)
    S1 = get_s(T[0], T[1])
    S2 = get_s(T[1], T[2])
    S4 = get_s(T[2], T[3])
    S8 = get_s(T[3], T[4])
    C1 = get_c(S1, S2)
    C2 = get_c(S2, S4)
    C3 = get_c(S4, S8)
    R1 = get_r(C1, C2)
    R2 = get_r(C2, C3)
    W1 = get_w(R1, R2)
    return W1


def sample_function_gauss_ch2(x):
    return e ** x


def sample_function(x):
    return (e ** x) * sqrt(1 - (x ** 2))


if __name__ == '__main__':
    print("gauss_ch2:")
    start_time = datetime.now()
    result = gauss_ch2(sample_function_gauss_ch2, 10000)
    end_time = datetime.now()
    print(f"result={result}")
    print(f"running time={(end_time - start_time).microseconds / 1000}ms")
    print()
    print("comp_gauss_leg:")
    start_time = datetime.now()
    result = comp_gauss_leg(sample_function, -1, 1)
    end_time = datetime.now()
    print(f"result={result}")
    print(f"running time={(end_time - start_time).microseconds / 1000}ms")
    print()
    print("comp_trep:")
    start_time = datetime.now()
    result = comp_trep(sample_function, -1, 1)
    end_time = datetime.now()
    print(f"result={result}")
    print(f"running time={(end_time - start_time).microseconds / 1000}ms")
    print()
    print("romberg:")
    start_time = datetime.now()
    result = romberg(sample_function, -1, 1)
    end_time = datetime.now()
    print(f"result={result}")
    print(f"running time={(end_time - start_time).microseconds / 1000}ms")
