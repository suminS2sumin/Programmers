from math import gcd

def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    a = gcd(numer, denom)
    numer //= a
    denom //= a
    return [numer, denom]