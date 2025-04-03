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
        for value, count in values:
            if count == 2:
                p = value
                break
        one_values = [v[0] for v in values if v[1] == 1]
        q, r = one_values[0], one_values[1]
        return q * r
            
    elif len(counter) == 4:
        answer = min(dice)
        
            
    return answer