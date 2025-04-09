def solution(myString, pat):
    sm = myString.replace("A", "C").replace("B", "A").replace("C", "B")
    if pat in sm:
        return 1
    else:
        return 0