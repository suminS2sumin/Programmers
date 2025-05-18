def solution(picture, k):
    answer = []
    for i in picture:
        a = ''.join(x * k for x in i)
        for _ in range(k):
            answer.append(a)
        
    return answer