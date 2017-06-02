def multiple(a, b):
    """Return the smallest number n that is a multiple of both a and b.

    >>> multiple(3, 4)
    12
    >>> multiple(14, 21)
    42
    """
    "*** YOUR CODE HERE ***"
    maximum = max(a, b)
    multiple_number = maximum
    minimum = min(a, b)
    i = 2
    while(multiple_number % minimum != 0):
        multiple_number = maximum * i
        i += 1
    return multiple_number

def unique_digits(n):
    """Return the number of unique digits in positive integer n

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    str_n = str(n)
    unique_digit_set = []
    s = set(unique_digit_set)
    for i in range(len(str_n)):
        s.add(str_n[i])
    return len(s)
