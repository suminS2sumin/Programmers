def solution(str_list):
    answer = []
    for i in str_list:
        if i == "l":
            answer = str_list[0:i]
            break
        elif i == "r":
            answer = str_list[i:]
            break
        else:
            answer = []
    return answer