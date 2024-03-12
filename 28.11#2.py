for A in range(1,1000):
    flag = True
    for x in range(1,1000):
        for y in range(1,1000):
            F = (x * y < A) or (x < y) or (9 < x)
            if F == 0:
                flag = False
    if flag:
        print(A)
        break