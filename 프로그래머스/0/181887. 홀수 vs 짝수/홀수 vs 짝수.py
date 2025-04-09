def solution(num_list):
    answer = 0
    a = 0
    b = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            a += num_list[i]
        elif i % 2 == 1:
            b += num_list[i]
    answer = max(a, b)
    return answer