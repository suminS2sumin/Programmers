def solution(arr, n):
    if len(arr) % 2 == 1:
        for i in range(0, len(arr), 2):
            arr[i] += n
    else:
        for j in range(1, len(arr) ,2):
            arr[j] += n   
    return arr