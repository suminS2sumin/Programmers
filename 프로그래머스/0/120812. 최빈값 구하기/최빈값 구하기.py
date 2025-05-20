def solution(array):
    count = {}
    for i in array:
        count[i] = count.get(i, 0) + 1

    max_count = max(count.values())
    max_keys = [k for k, v in count.items() if v == max_count]
    return max_keys[0] if len(max_keys) == 1 else -1 