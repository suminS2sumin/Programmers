def solution(a, b, c):
    answer = a + b + c
    
    if a != b != c:
        answer
    
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        answer *= (a ** 2 + b ** 2 + c ** 2)
        
    if a == b == c:
        answer *= (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)
        
    return answer