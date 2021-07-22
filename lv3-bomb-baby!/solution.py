def solution(x, y):
    # Your code here
    ctr = 0
    x, y = int(x), int(y)
    while x != 1 and y != 1:
        if x % y == 0:
            return 'impossible'
        else:
            ctr += int(max(x, y)/min(x, y))
            x, y = max(x, y) % min(x, y), min(x, y)
    return str(ctr+max(x, y)-1)
