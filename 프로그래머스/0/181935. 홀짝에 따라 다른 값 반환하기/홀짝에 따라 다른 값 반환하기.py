def solution(n):
    answer = 0
    if (n % 2 == 1):
        return sum(i for i in range(1, n+1, 2))
    
    if (n % 2 == 0):
        return sum(i ** 2 for i in range(2, n+1, 2))
            
    return sum