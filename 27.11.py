for A in range(1,1000):
    Flag = True
    for x in range(1,1000):
        F = ((x & 29!=0) <= ((x & 17 == 0) <= (x & A !=0)))
        if F == 0:
            Flag = False
    if Flag:
        print(A)
        break
