def solution(arr, idx):
    
    for i in range(idx):
        del arr[0]
        
    for j in range(len(arr)):
        if arr[j] == 1:
            return j + idx
        
    return -1