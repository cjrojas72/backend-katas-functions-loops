#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """
import operator

__author__ = "Christian Rojas"


def add(x, y):
    """Add two integers. Handles negative values."""
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    value = 0

    for num in range(abs(y)):
        value = add(value, abs(x))

    if x < 0 and y < 0:
        return value
    elif x < 0 or y < 0:
        return -value
    else:
        return value


def power(x, n):
    """Raise x to power n, where n >= 0"""
    value = x
    if n == 0:
        return 1
    else:
        for num in range(1, n):
            value = multiply(value, x)
    return value


def factorial(x):
    """Compute factorial of x, where x > 0"""
    f = 1
    if x >= 1:
        for i in range(1, add(x, 1)):
            f = multiply(f, i)
    return f


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 2 or n == 1:
        return 1
    else:
        return add(fibonacci(n-1), fibonacci(n-2))


if __name__ == '__main__':
    # your code to call functions above
    pass
