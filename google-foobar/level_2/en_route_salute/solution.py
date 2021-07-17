def solution(s):
    persons = 0
    count = 0
    for c in s:
        if c == ">":
            persons += 1
        if c == "<":
            count += persons
    
    return count*2