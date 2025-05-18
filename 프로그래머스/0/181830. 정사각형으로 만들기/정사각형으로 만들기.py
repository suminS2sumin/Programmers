def solution(arr):
    n, m = len(arr), len(arr[0])
    if n > m:
        for i in range(n):
            while len(arr[i]) < n:
                arr[i].append(0)
            
    elif n < m:
        for _ in range(m - n):
            arr.append([0] * m)
                
    else:
        pass
                
    return arr
    
                                