def f(s, d):
    if s  >= 108: return d%2==0
    if d == 0: return 0
    if s%2==0:
        h = [f(s+1,d-1), f(s*1.5,d-1)]
    else:
        h = [f(s+1,d-1), f(s*2, d-1)]
    return any(h) if d % 2 != 0 else all(h)

# def f1(s, d):
#     if s  >= 108: return d%2==0
#     if d == 0: return 0
#     if d%2==0:
#         h = [f(s+1,d-1), f(s*2,d-1)]
#     else:
#         h = [f(s*1.5, d-1)]
#     return any(h) if d % 2 != 0 else any(h)

print(max([s for s in range(1,108) if f(s,2)]))
print(*[s for s in range(1,108) if f(s,3) and not f(s,1)])
print(*[s for s in range(1,108) if f(s,4) and not f(s,2)])