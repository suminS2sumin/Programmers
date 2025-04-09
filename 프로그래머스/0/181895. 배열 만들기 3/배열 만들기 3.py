def solution(arr, intervals):
    answer = []
    (a, b), (c, d) = intervals
    answer.extend(arr[a:b+1] + arr[c:d+1])
    return answer