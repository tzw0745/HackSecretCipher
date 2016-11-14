# !/usr/bin/env python
# coding:utf-8
"""
Created by tzw0745 on 2016/10/27.
chapter 14
"""


def GCD(a, b):
    """
    求最大公约数
    :param a: 整数a
    :param b: 整数b
    :return: a和b的最大公约数
    """
    while a != 0:
        a, b = b % a, a

    return b


def ModInverse(a, m):
    """
    欧几里得扩展算法求a和b的模逆
    :param a: 整数a
    :param m: 整数m
    :return: a和m的模逆
    """
    # 如果a和m不互质则不存在模逆
    if GCD(a, m) != 1:
        return None

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        # q只保留整数
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % m


def main():
    print(ModInverse(8953851, 26))


if __name__ == '__main__':
    main()
