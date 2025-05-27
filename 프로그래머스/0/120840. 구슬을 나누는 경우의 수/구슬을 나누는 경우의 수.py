def solution(balls, share):
    b, s, bs = 1, 1, 1
    for x in range(balls):
        b *= x + 1
    for y in range(share):
        s *= y + 1
    for z in range(balls - share):
        bs *= z + 1
    return b / (bs * s)