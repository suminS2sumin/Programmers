def solution(num_list, n):
    answer = []
    for i in range(len(num_list)):
        answer = num_list[n:]
    answer += num_list[0:n]
    return answer