def solution(n):
    # Your code here
    n = int(n)
    ctr = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
            ctr += 1
        else:
            if ((n - 1)/2) % 2 == 0 or n == 3:
                n -= 1
                ctr += 1
            else:
                n += 1
                ctr += 1
    return ctr
