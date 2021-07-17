import math

def solution(total_lambs):
    least = int(math.log(total_lambs + 1, 2))
    most = fib(total_lambs)
    return most - least


def fib(n):
    if n <= 2:
        return n
    
    r = n - 2
    count = 2
    l = 1
    ll = 1
    while r >= l + ll:
        r -= l
        r -= ll
        previous = ll
        ll = l
        l += previous
        count += 1
    
    return count