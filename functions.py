import math as m


def xt(t):
    x = 16 * m.sin(t) ** 3
    return x


def yt(t):
    y = 13 * m.cos(t) - 5 * m.cos(2 * t) - 2 * m.cos(3 * t) - m.cos(4 * t)
    return y
