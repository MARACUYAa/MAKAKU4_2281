def f(s1,s2,d):
    if s1+s2 >= 133: return d % 2 == 0
    if d == 0: return 0
    h = [f(s1 + 1,s2,d-1), f(s1 * 4,s2,d-1), f(s1,s2+1,d-1),f(s1,s2*4,d-1)]
    return any(h) if d % 2!=0 else all(h)
def f1(s1,s2,d):
    if s1+s2 >= 133: return d % 2 == 0
    if d == 0: return 0
    h = [f(s1 + 1,s2,d-1), f(s1 * 4,s2,d-1), f(s1,s2+1,d-1),f(s1,s2*4,d-1)]
    return any(h) if d % 2!=0 else any(h)
print(*[s for s in range(1,126) if f1(7,s,2)][:1])
print(*[s for s in range(1,126) if f(7,s,3) and not f(7,s,1)])
print(*[s for s in range(1,126) if f(7,s,4) and not f(7,s,2)])
    
    