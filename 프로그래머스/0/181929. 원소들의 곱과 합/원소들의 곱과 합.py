def solution(num_list):
    answer = 0
    Plus_sum = sum(num_list)
    Multiply_sum = 1
    
    for i in range(len(num_list)):
        Multiply_sum *= num_list[i]
        
    answer = int(bool(Multiply_sum < Plus_sum ** 2))
    
    return answer