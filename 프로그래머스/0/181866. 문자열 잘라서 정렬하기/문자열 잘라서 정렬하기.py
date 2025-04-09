def solution(myString):
    sm = myString.split("x")
    sm = [x for x in sm if x != ""]
    return sorted(sm)