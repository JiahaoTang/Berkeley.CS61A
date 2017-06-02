HW_SOURCE_FILE = 'hw04.py'
import math
def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> g(6)
    51
    >>> g(7)
    125
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)
def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    
    g1, g2, g3 = 1, 2, 3
    upper, count = 0, 4
    while count <= n:
        upper = g3 + 2 * g2 + 3 * g1
        g3, g2, g1 = upper, g3, g2
        count += 1
    
    return upper


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    """
    number = 0
    switch = True
    for i in range(n):
        if switch == True:
            number_plus(number)
        else:
            number_sub(number)
        if has_seven(i + 1) or (i + 1) % 7 == 0:
            switch_value(switch)
    return number
    """
    def find(i, switch):
        if i == n:
            if switch == True:
                return 1
            else:
                return -1

        if i < n :
            if switch == True:
                if has_seven(i) or i % 7 == 0:
                    return 1 + find(i + 1, False)
                else:
                    return 1 + find(i + 1, True)
            else:
                if has_seven(i) or i % 7 == 0:
                    return -1 + find(i + 1, True)
                else:
                    return -1 + find(i + 1, False)
    return find(1, True)

def has_seven(k):
    
    
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    def count_partitions(n, m):
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 1:
            return 1
        else:
            return count_partitions(n - m, m) + count_partitions(n, m / 2)
    return count_partitions(amount, 2**(int(math.log(amount, 2))))
###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return lambda n, f = lambda n, f: 1 if n == 1 else mul(n, f(sub(n, 1), f:f(n, f)))
