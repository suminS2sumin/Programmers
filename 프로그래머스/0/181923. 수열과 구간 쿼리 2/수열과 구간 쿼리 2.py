def solution(arr, queries):
    answer = []
    for a in range(len(queries)):
        s = queries[a][0]
        i = queries[a][1]
        k = queries[a][2]
        
        filter_answer = [x for x in arr[s:i+1] if x > k]
        
        if filter_answer:
            answer += [min(filter_answer)]
        else:
            answer += [-1]
    return answer