for a in range(1,1000):
    flag = True
    for x in range(1,1000):
        F = (x&25 != 0) <= ((x&19 == 0) <= (x&a != 0))
        if F == 0:
            flag = False
    if flag:
        print(a)
        break