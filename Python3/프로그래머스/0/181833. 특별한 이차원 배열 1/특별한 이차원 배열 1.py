def solution(n):
    return [[int(x == y) for x in range(n)] for y in range(n)]