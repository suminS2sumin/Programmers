def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        i_str = str(i)
        if all(digit in '50' for digit in i_str):
            answer += [i]
    if not answer:
        answer += [-1]
    return answer