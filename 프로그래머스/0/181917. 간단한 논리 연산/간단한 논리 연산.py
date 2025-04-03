def solution(x1, x2, x3, x4):
    answer = True
    b1 = True
    b2 = True
    
    if bool(x1) or bool(x2):
        b1 = True
    elif not bool(x1) and not bool(x2):
        b1 = False
        
    if bool(x3) or bool(x4):
        b2 = True
    elif not bool(x3) and not bool(x4):
        b2 = False
        
    if b1 and b2:
        answer = True
    elif not b1 or not b2:
        answer = False
        
    return answer