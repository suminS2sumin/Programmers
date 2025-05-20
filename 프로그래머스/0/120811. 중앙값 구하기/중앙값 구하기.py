def solution(array):
    array.sort()
    return array[len(array) - len(array) // 2 - 1]