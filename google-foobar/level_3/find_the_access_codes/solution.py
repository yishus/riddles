def solution(l):
    c = [0] * len(l)
    count = 0
    for i in range(len(l)):
        for j in range(i):
            if l[i] % l[j] == 0:
                c[i] += 1
                count += c[j]
    return count