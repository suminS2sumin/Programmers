def solution(code):
    mode = 0
    ret = ""

    for idx in range(len(code)):
        if code[idx] == "1":
            mode = 1 - mode

        else:
            if (mode == 0 and idx % 2 == 0) or (mode == 1 and idx % 2 == 1):
                ret += code[idx]

    return ret if ret else "EMPTY"

