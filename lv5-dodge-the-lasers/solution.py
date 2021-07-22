import math


def t(n):
    return n*4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727/10**100
    #return math.floor(n*(math.sqrt(2)-1))


def s(n):
    if n == 0:
        return 0
    return n*t(n)+n*(n+1)/2-t(n)*(t(n)+1)/2-s(t(n))


def solution(n):
    # Your code here
    return str(int(s(int(n))))


print(solution(5))
