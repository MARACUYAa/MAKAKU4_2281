# #25
# from fnmatch import fnmatch
# for i in range(0,10**8,273):
#     if fnmatch(str(i), '12??36*1'):
#         print(i,i//273)
# #24
# a = open('24_7600.txt').readline()
# s = a.replace('Q','*').replace('R','*').replace('S','*')
# s = s.replace('**', ' $ ')
# s = s.split(' $ ')
# print(max(list(map(len, s)))+2)
#23
# def f(x,y):
#     if x == y:
#         return 1
#     if x > y or x == 13:
#         return 0
#     return f(x+1,y) + f(x+2,y) + f(x * 3, y)
# print(f(3,8)+f(8,18))
# #19-21
# def f(s,d):
#     if s >= 78: return d%2==0
#     if d == 0: return 0
#     h = [f(s+1,d-1),f(s+4,d-1),f(s*4,d-1)]
#     return any(h) if d % 2 != 0 else all(h)
# print([s for s in range(1,78) if f(s,2)])
# print([s for s in range(1,78) if f(s,3) and not f(s,1)])
# print([s for s in range(1,78) if f(s,4) and not f(s,2)])
# #16
# from sys import *
# setrecursionlimit(10**6)
# def f(n):
#     if n >= 2025: return n
#     if n < 2025: return n + 3 + f(n + 3)
# print(f(23)-f(21))
#15
# for a in range(100):
#     flag = 1
#     for x in range(100):
#         f = ((x & 39 == 0) or ((x&11 ==0) <= (not(x&a == 0))))
#         if f == 0:
#             flag = 0
#     if flag == 1:
#         print(a)
# #14
# for x in range(0,15):
#     a = int(f'97968{x}13', 15)
#     b = int(f'7{x}213',15)
#     if (a+b)%14 == 0:
#         print((a + b)/14)

from ipaddress import *
k = 0
net = ip_network('203.153.0.0/255.255.0.0', 0)
for a in net:
    s = f'{a:b}'
    if s[-1] == '0':
        k += 1
print(k)
