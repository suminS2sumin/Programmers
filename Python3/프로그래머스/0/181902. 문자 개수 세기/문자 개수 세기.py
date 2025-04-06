def solution(my_string):
    answer = []
    asc = [ord(c) for c in my_string]
    for i in range(65, 91, 1):
        answer.append(asc.count(i))
    for j in range(97, 123, 1):
        answer.append(asc.count(j))  
    return answer