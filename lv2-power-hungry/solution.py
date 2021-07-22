def solution(xs):
    # Your code here
    prod = 1
    arr_neg = [i for i in xs if i < 0]

    if len(xs) == 1:
        return str(xs[0])

    if len([i for i in xs if i > 0]) == 0 and len(arr_neg) == 1:
        return str(0)

    if len(arr_neg) % 2 == 0 and len(arr_neg) != 0:
        for i in xs:
            if i != 0:
                prod *= i
        return str(prod)

    if len(arr_neg) == 0:
        big_pos = 1
    else:
        big_pos = max(arr_neg)

    for i in xs:
        if i != 0:
            prod *= i

    return str(prod/big_pos)
