def solution(order):
    sum = 0
    for i in order:
        if "cafelatte" in i:
            sum += 5000
        else:
            sum += 4500
    return sum
                