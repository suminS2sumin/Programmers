def solution(a, b):
    answer1 = str(a) + str(b)
    answer2 = str(b) + str(a)
    
    return int(max(answer1, answer2))