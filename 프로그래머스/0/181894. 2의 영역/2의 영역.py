def solution(arr):
    answer = []
    two = []
    for i in range(len(arr)):
        if arr[i] == 2:
            two.append(i)
    if two:
        return arr[min(two):max(two)+1]
    else:
        return [-1]