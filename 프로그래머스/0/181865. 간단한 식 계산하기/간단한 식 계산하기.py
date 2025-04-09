def solution(binomial):
    sb = binomial.split()
    if sb[1] == '+':
        return int(sb[0]) + int(sb[2])
    elif sb[1] == '-':
        return int(sb[0]) - int(sb[2])
    else:
        return int(sb[0]) * int(sb[2])