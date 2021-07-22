def solution(n, b):
    # Your code here
    l = []
    strlen = len(str(n))
    while l.count(n) == 0:
        l.append(int(n))
        x = "".join(sorted(str(n)))
        y = "".join(sorted(str(n).zfill(strlen), reverse=True))
        n = int(y, b) - int(x, b)
        n = int(to_base(n, b))
    if l.pop() == n:
        return 1
    return len(l)-l.index(n)+1


BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(n, b):
    return "0" if not n else to_base(n//b, b).lstrip("0") + BS[n % b]
