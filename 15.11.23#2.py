def f(s,d):
    if s > 42: return d%2!=0
    if s == 42: return d%2==0
    if d==0: return 0
    h = [f(s+1, d-1), f(s+3, d-1), f(s+7, d-1)]
    return any(h) if d % 2 != 0 else all(h)
print(*[s for s in range(1, 43) if f(s,2) and not f(s,1)])
print(*[s for s in range(1, 43) if f(s,3)])
print(*[s for s in range(1, 43) if f(s,4) and not f(s,2)])
