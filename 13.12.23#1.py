def prost(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
def prost_delit(x):
    a = []
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            if prost(i):
                a.append(i)
            if prost(x//i):
                a.append (x//i)
    return(sorted(set(a)))
for x in range(25317,51238):
    a = prost_delit(x)
    if len(a) >= 6:
        print(x, a[-1])
