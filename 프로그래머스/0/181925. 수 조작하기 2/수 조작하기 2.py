def solution(numLog):
    result = ''
    for i in range(len(numLog) - 1):
        if numLog[i + 1] - numLog[i] == 1:
            result += 'w'
        if numLog[i + 1] - numLog[i] == -1:
            result += 's'
        if numLog[i + 1] - numLog[i] == 10:
            result += 'd'
        if numLog[i + 1] - numLog[i] == -10:
            result += 'a'
    return result