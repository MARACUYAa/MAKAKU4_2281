# k = 0
# for x1 in 'aqkoc':
#     for x2 in 'aqkoc':
#         for x3 in 'aqkoc':
#             for x4 in 'aqkoc':
#                 for x5 in 'aqkoc':
#                     s = x1+x2+x3+x4+x5
#                     k += 1
#                     if s.count('o') < 2 and ('cc' not in s):
#                         print(k)

# k = 0
# for x1 in '12345678':
#     for x2 in '012345678':
#         for x3 in '012345678':
#             for x4 in '012345678':
#                 for x5 in '012345678':
#                         s = x1 + x2 + x3 + x4 + x5
#                         s2 = s.replace('2', '0').replace('4', '0').replace('6', '0').replace('8', '0')
#                         if s.count('1') == 1 and ('10' not in s2) and ('01' not in s2):
#                             k += 1
# print(k)

# from sys import setrecursionlimit
# from functools import lru_cache
# setrecursionlimit(10000)
# def F(n):
#     if n>= 2025:
#         return n
#     if n < 2025:
#         return n + 3 + F(n + 3)
# print(F(23) - F(21))

# def F(n):
#     if n == 1:
#         return 1
#     if n % 2 == 0:
#         return n + F(n - 1)
#     if n > 1 and n % 2 != 0:
#         return 2 * F(n-2)
# print(F(26))

# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     if n > 2 and n % 2 == 0:
#         return (3*n + F(n - 3))//3
#     if n > 2 and n % 2 != 0:
#         return (7 * n + F(n - 1) - F(n - 2)) // 5
# print(F(35))

# def F(n):
#     if n == 0:
#         return 0
#     if n > 0 and n% 2 ==0:
#         return F(n/2)
#     if n%2!=0:
#         return 1 + F(n - 1)
# k = 0
# for n in range(1, 1001):
#     if F(n) == 3:
#         k +=1
# print(k)

# def F(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 1
#     if n > 2:
#         return F(n - 2) * (n - 1)
# print(F(7))

# def F(n):
#     if n == 1:
#         return 0
#     if n > 1:
#         return F(n-1) + n
# def G(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return G(n-1) * n
# print(F(5) + G(5))

# def H(x):
#     if x < 3:
#         return 1
#     if x > 2:
#         return 2*x - 1 + H(x-2)
# print(H(3033))
# @lru_cache()
# def F(n):
#     if n < 3:
#         return n
#     if n > 2:
#         return (2*n-1)* (F(n-1) + F(n-2))
# print(F(69) % (10**9 +7))


# for A in range(1, 1000):
#     flag = 1
#     for x in range(1, 1000):
#         F = ((x%A != 0) <= ((x%6 == 0) <= (x%4!= 0)))
#         if F == 0:
#             flag = 0
#     if flag == 1:
#         print(A)

# def F(n):
#     if n ==1:
#         return 1
#     if n == 2:
#         return 2
#     if n > 2 and n % 2 == 0:
#         return int((4*n - F(n-3))/8)
#     if n > 2 and n % 2 != 0:
#         return int((4*n-F(n-1) + F(n-2))/8)
# print(F(52) - F(38))

# def F(n):
#     if n <= 1:
#         return 0
#     if (n>1) and (n%2!=0):
#         return F(n-1) + 3*n**2
#     if (n>1) and (n%2==0):
#         return n/2 + F(n-1) + 2
# print(F(49))
from sys import setrecursionlimit
setrecursionlimit(1000000)
from functools import lru_cache

# def F(n):
#     if n<3:
#         return 2**1024
#     if n>2:
#         return 2*n+3+F(n-2)
# print(F(4048) - F(16))

# def s(x):
#     return sum(map(int, str(x)))
#
# @lru_cache()
# def F(n):
#     if n == 0:
#         return 1
#     if n>0:
#         return 2*F(1-n)+3*F(n-1)+2
#     if n<0:
#         return (-1) * F(-n)
# print(s(F(50)))
# k = 0
# a = []
# @lru_cache()
# def F(n):
#     if n<3:
#         return n+1
#     if n>=3 and n%2==0:
#         return F(n-2) + n - 2
#     if n >= 3 and n % 2 != 0:
#         return F(n+2) + n + 2
# for n in range(2, 10000,2):
#     x = F(n)
#     if len(str(x)) == 5:
#         a.append(x)
# print(len(set(a)))

















