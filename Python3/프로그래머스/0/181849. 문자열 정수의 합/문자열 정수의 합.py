def solution(num_str):
    sum = 0
    for i in range(len(num_str)):
        sum += int(num_str[i])    
    return sum