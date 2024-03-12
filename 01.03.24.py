# def f(s,d):
#     if s >= 429: return d % 2==0
#     if d == 0: return 0
#     h = [f(s+5,d-1),f(s*5,d-1)]
#     return any(h) if d % 2 != 0 else all(h)
# print([s for s in range(1, 429) if f(s,2)])
# print([s for s in range(1, 429) if f(s,3) and not f(s,1)])
# print([s for s in range(1, 429) if f(s,4) and not f(s,2)])

# def f(s,s1,d):
#     if s+s1 >=342: return d % 2 == 0
#     if d == 0: return 0
#     h = [f(s+2,s1,d-1),f(s*5,s1,d-1),f(s,s1+2,d-1),f(s,s1*5,d-1)]
#     return any(h) if d % 2 != 0 else all(h)
# print([s1 for s1 in range(1,326) if f(11,s1,2)])#14
# print([s1 for s1 in range(1,326) if f(11,s1,3) and not f(11,s1,1)])
# print([s1 for s1 in range(1,326) if f(11,s1,4) and not f(11,s1,2)])

# def f(s,s1,d):
#     if 110 >= s*s1 >=70: return d % 2 == 0
#     if s*s1 >=110: return d % 2 != 0
#     if d == 0: return 0
#     h = [f(s+1,s1,d-1),f(s*2,s1,d-1),f(s,s1+1,d-1),f(s,s1*2,d-1)]
#     return any(h) if d % 2 != 0 else all(h)
# print([s1 for s1 in range(1,66) if f(5,s1,2)])#4
# print([s1 for s1 in range(1,66) if f(5,s1,3) and not f(5,s1,1)])
# print([s1 for s1 in range(1,66) if f(5,s1,4) and not f(5,s1,2)])

def f(s, d):
    if s < 117: return d % 2 == 0
    if d == 0: return 0
    h = [f(s-7,d-1),f(s/3,d-1)]
    return any(h) if d % 2 != 0 else all(h)
print([s for s in range(117,10001) if f(s,3) and not f(s,1)]) #3158
print([s for s in range(117,10001) if f(s,3) and not f(s,1)])
print([s for s in range(117,10001) if f(s,4) and not f(s,2)])