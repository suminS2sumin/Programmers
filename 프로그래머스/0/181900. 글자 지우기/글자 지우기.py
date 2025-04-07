def solution(my_string, indices):
    answer = ''
    sort_indices = sorted(indices, reverse = True)
    l_string = list(my_string)
    
    for i in sort_indices:
        del l_string[i]
        
    answer = ''.join(l_string)
    return answer