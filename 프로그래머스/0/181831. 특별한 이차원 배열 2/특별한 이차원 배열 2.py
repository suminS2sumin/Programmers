def solution(arr):
    return int(all(arr[j][i] == arr[i][j] for i in range(len(arr))for j in range(len(arr))))      