def f(s, d):
    if s  >= 100: return d%2==0
    if d == 0: return 0
    h = [f(s+2,d-1), f(s+4,d-1), f(s*2,d-1)]
    return any(h) if d % 2 != 0 else all(h)
def f1(s, d):
    if s  >= 100: return d%2==0
    if d == 0: return 0
    h = [f(s+2,d-1), f(s+4,d-1), f(s*2,d-1)]
    return any(h) if d % 2 != 0 else any(h)
print(*[s for s in range(1,108) if f1(s,1)])
print(*[s for s in range(1,108) if f(s,4) and not f(s,2)])
print(*[s for s in range(1,108) if f(s,3) and not f(s,1)])