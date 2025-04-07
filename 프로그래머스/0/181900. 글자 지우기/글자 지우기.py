def solution(my_string, indices):
    sort_indices = sorted(indices, reverse = True)
    l_string = list(my_string)
    
    for i in sort_indices:
        del l_string[i]
        
    return ''.join(l_string)