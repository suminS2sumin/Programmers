def solution(myString):
    ms = myString.replace("a", "A")
    ms = list(ms)
    for i in range(len(ms)):
        if ms[i] != "A":
            ms[i] = ms[i].lower()
    return ''.join(ms)