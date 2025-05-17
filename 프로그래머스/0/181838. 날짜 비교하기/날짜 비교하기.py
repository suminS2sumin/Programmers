def solution(date1, date2):
    return int(int("".join(str(x) for x in date1)) < int("".join(str(y) for y in date2)))