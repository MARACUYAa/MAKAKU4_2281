for A in range(1,1000):
    flag = True
    for x in range(1,1000):
        for y in range(1,1000):
            F = (x + 2*y > A) or (y < x) or (x < 30)
            if F == 0:
                flag = False
    if flag:
        print(A)