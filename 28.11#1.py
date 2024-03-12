for A in range(1,1000):
    flag = True
    for x in range(1,1000):
        for y in range(1,1000):
            F = (x < A) or (y < A) or (x + 2*y > 50)
            if F == 0:
                flag = False
    if flag:
        print(A)
        