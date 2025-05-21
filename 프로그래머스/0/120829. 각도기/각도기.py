def solution(angle):
    return 2 if angle / 90 == 1.0 else 4 if angle / 90 == 2.0 else 1 if angle // 90 == 0 else 3 