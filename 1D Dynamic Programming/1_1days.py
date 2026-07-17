def climbstair(n):
    if n <= 2:
        return n

    one = 1
    two = 2

    for i in range(3,i+1):
        cur = one + two
        two = one
        one = cur

    return one