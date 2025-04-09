def solution(nl):
    sum = 0
    for i in range(len(nl)):
        while(nl[i] != 1):
            sum += 1
            nl[i] = nl[i] // 2
    return sum