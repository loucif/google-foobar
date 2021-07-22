def solution(l):
    # Your code here
    ctr = 0

    if len(l) < 3:
        return 0

    for i, mid in enumerate(l):
        ctr += sum(1 for x in l[:i] if mid % x == 0) * \
            sum(1 for x in l[i+1:] if x % mid == 0)

    return ctr
