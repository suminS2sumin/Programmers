def solution(my_string):
    return "".join([x for x in my_string if x not in ("aeiou")])