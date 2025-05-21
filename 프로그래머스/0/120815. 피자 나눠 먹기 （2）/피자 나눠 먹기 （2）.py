def solution(n):
    return n // max({x for x in range(1, n+1) if n % x == 0} & {1, 2, 3, 6})