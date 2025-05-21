def solution(my_string, n):
    return "".join([my_string[x] * n for x in range(len(my_string))])