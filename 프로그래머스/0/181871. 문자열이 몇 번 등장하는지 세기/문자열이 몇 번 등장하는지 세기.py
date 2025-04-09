def solution(myString, pat):
    answer = 0
    sf = 0
    while True:
        sf = myString.find(pat, sf)
        if sf == -1:
            break
        answer += 1
        sf += 1
    return answer
            