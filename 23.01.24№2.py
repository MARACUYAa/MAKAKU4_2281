# k = 0
# for x1 in 'vina':
#     for x2 in 'visna':
#         for x3 in 'visna':
#             for x4 in 'visna':
#                 for x5 in 'visna':
#                     for x6 in 'vsn':
#                         s = x1 + x2 + x3 + x4 + x5 + x6
#                         if s.count('v') <= 1:
#                             k +=1
#     print(k)
# k = 0
# for x1 in 'NIKOLA':
#     for x2 in 'NIKOLAY':
#         for x3 in 'NIKOLAY':
#             for x4 in 'NIKOLAY':
#                 s = x1 + x2 + x3 + x4
#                 s= s.replace('O', 'A').replace('I', 'A')
#                 if s.count('A') > 0:
#                     k +=1
# print(k)
# k = 0
# for x1 in 'ruslan':
#     for x2 in 'ruslan':
#         for x3 in 'ruslan':
#             for x4 in 'ruslan':
#                 for x5 in 'ruslan':
#                     for x6 in 'ruslan':
#                         s = x1 + x2 + x3 + x4 + x5 + x6
#                         s2 = s.replace('u', 'a')
#                         if len(set(s)) == len(s) and ('aa' not in s2):
#                             k+=1
# print(k)
# k =0
# for x1 in '1234567':
#     for x2 in '01234567':
#         for x3 in '01234567':
#             for x4 in '01234567':
#                 for x5 in '01234567':
#                         s = x1 + x2 + x3 + x4 + x5
#                         s = s.replace('3', '1').replace('5', '1').replace('7', '1')
#                         if s.count('1') <= 2:
#                             k +=1
# print(k)
# k =0
# for x1 in '1234567':
#     for x2 in '01234567':
#         for x3 in '01234567':
#             for x4 in '01234567':
#                 for x5 in '01234567':
#                         s = x1 + x2 + x3 + x4 + x5
#                         s2 = s.replace('3', '1').replace('5', '1').replace('7', '1').replace('2', '0').replace('4', '0').replace('6', '0')
#                         if len(set(s)) == len(s) and ('11' not in s2) and ('00' not in s2):
#                             k +=1
# print(k)
# k = 0
# for x1 in '12345678':
#     for x2 in '012345678':
#         for x3 in '012345678':
#             for x4 in '012345678':
#                 for x5 in '012345678':
#                         s = x1 + x2 + x3 + x4 + x5
#                         s2 = s.replace('3', '1').replace('5', '1').replace('7', '1').replace('9', '1')
#                         if s.count('3') == 2 and ('12' not in s2) and ('21' not in s2):
#                             k+=1
# print(k)


# k = 0
# for x1 in 'aklmny':
#     for x2 in 'aklmny':
#         for x3 in 'aklmny':
#             for x4 in 'aklmny':
#                 s = x1+x2+x3+x4
#                 k += 1
#                 if x1 == 'k' and x2 == 'm':
#                     print(k)
#                     break

