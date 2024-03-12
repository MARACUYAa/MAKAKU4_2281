# s = '8' * 84
# while '1111' in s or '8888' in s:
#     if '1111' in s:
#         s = s.replace('1111', '8', 1)
#     else:
#         s = s.replace('8888', '11', 1)
# print(s)

# s = 91 * '8'
# while '3333' in s or '8888' in s:
#     if '3333' in s:
#         s = s.replace('3333', '8', 1)
#     else:
#         s = s.replace('8888', '33', 1)
# print(s)
# a = []
# for i in range(100, 1000):
#     s = '1'*i
#     s0 = s
#     while '111' in s or '88888' in s:
#         if '111' in s:
#             s = s.replace('111' , '88', 1)
#             a.append(s)
#         else:
#             s = s.replace('88888', '8', 1)
#             a.append(s)
#     print(i, s)
# a= []
# for i in range(1, 1000):
#     s = '1' * i
#     while '1111' in s or '222' in s or '33' in s:
#         if '1111' in s:
#             s = s.replace('1111', '333', 1)
#         elif '222' in s:
#             s = s.replace('222','11',1)
#         else:
#             s = s.replace('33', '2', 1)
#     a.append(s)
# print(len(set(a)))

# s = '1' + '8' * 99 + '1'
# while '81' in s or '882' in s or '8883' in s:
#     if '81' in s:
#         s = s.replace('81', '2', 1)
#     elif '882' in s:
#         s = s.replace('882', '3', 1)
#     else:
#         s = s.replace('8883', '1', 1)
# print(s)
# for i in range(200, 1000):
#     s = '1' * i
#     s0 = s
#     while '1111' in s:
#         s = s.replace('1111', '22', 1).replace('222', '1', 1)
#     print(len(s0),s.count('1'))
# for i in range(1, 50):
#     for x in range(1, 50):
#         for y in range(1, 50):
#             s = '0' + '1' * i + '2' * x + '3' * y + '0'
#             s0 = s
#             while '00' not in s:
#                 s = s.replace('01', '201', 1).replace('02', '3101', 1).replace('03', '2012',1)
#             if s.count('1') == 61 and s.count('2') == 50 and s.count('3') == 18:
#                  print(len(s0), s)




def prost(x):
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True
def summ(z):
    return sum(map(int,str(z)))
a = []
for x in range(1, 100):
    for y in range(1, 100):
        s = '0' + '1' * x + '2' * y
        s0 = s
        if len(s) > 44:
            while '01' in s or '02' in s:
                s = s.replace('02', '1110', 1).replace('01', '220', 1)
            if prost(summ(s)):
                a.append(summ(s0))
print(min(a))

