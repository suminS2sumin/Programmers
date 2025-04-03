from collections import Counter

def solution(a, b, c, d):
    answer = 0
    dice = [a, b, c, d]
    counter = Counter(dice)
    values = list(counter.items())
    
    if len(counter) == 1:
        answer = a * 1111
    
    elif len(counter) == 2:
        if values[0][1] == 3:
            p = values[0][0]
            q = values[1][0]
            answer = (10 * p + q) ** 2  
        elif values[1][1] == 3:
            p = values[1][0]
            q = values[0][0]
            answer = (10 * p + q) ** 2 
            
        elif values[0][1] == 2 and values[1][1] == 2:
            p = values[0][0]
            q = values[1][0]
            answer = (p + q) * abs(p - q)
            
            
    elif len(counter) == 3:
        
        if values[0][1] == 2:
            q = values[1][0]
            r = values[2][0]
            answer = q * r
        elif values[1][1] == 2:
            q = values[0][0]
            r = values[2][0]
            answer = q * r    
        elif values[2][1] == 2:
            q = values[1][0]
            r = values[0][0]
            answer = q * r
            
    elif len(counter) == 4:
        answer = min(dice)
        
            
    return answer