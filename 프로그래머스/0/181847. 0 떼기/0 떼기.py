def solution(n_str):
    if n_str[0] == "0":
        return n_str.lstrip("0")
    else:
        return n_str