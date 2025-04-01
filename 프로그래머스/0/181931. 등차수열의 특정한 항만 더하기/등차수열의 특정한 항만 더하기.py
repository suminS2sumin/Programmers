def solution(a, d, included):
    result = 0
    for i in range(len(included)):
        if included[i] == bool(1):
            result += a + i * d
    
    return result