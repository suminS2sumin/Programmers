def solution(myString):
    answer = []
    sm = myString.split("x")
    for i in sm:
        answer.append(len(i))
    return answer