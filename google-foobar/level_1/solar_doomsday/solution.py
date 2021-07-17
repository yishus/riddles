import math

def solution(area):
    values = []
    r = area
    while(r > 0):
        root = math.floor(math.sqrt(r))
        values.append(int(root * root))
        r -= root * root
    return values