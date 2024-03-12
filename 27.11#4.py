for a in range(1,1000):
    flag = True
    for x in range(1,1000):
        for y in range(1,1000):
            F = ((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9))
            if F == 0:
                flag = False
    if flag:
        print(a)
        