def solution(arr):
    x = 0
    while True:
        changed = False
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                arr[i] = arr[i] // 2
                changed = True
            elif arr[i] < 50 and arr[i] % 2 == 1:
                arr[i] = arr[i] * 2 + 1
                changed = True
        if changed:
            x += 1
        else:
            break
    return x