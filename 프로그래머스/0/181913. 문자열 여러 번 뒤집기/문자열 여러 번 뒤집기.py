def solution(my_string, queries):
    my_string = list(my_string)
    
    for i in queries:
        start, end = i[0], i[1]
        my_string[start:end+1] = my_string[start:end+1][::-1]
        
    answer = ''.join(my_string)
    return answer