def solution(n):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    a, b = 0, 0
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    da = 0
    
    for i in range(n * n):
        answer[a][b] = i+1
        
        db, dc = direction[da]
        next_a = a + db
        next_b = b + dc
        
        if next_a < 0 or next_b < 0 or next_a >= n or next_b >= n or answer[next_a][next_b] != 0:
            da = (da + 1) % 4
            db, dc = direction[da]
            next_a = a + db
            next_b = b + dc
        
        a, b = next_a, next_b
        
    return answer
    