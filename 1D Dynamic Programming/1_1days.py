def climbstair(n):
    if n <= 2:
        return n

    one = 1
    two = 2

    for i in range(3,n+1):
        cur = one + two
        one = two
        two = cur

    return two