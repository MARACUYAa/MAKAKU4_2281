# from ipaddress import *
#
# def sum_dig(x):
#     s = 0
#     for i in str(x):
#         if i != '.':
#             s += int(i)
#     return s
# a = sum_dig('95.122.230.120')
# for i in range(33):
#     net = ip_network(f"95.122.230.120/{i}", 0)
#     if a < sum_dig(str(net[0])):
#         print(net, net.netmask, i)

# for A in range(1,10000):
#     Flag = 1
#     for x in range(1, 10000):
#         if ((x & 39 == 0) or (x&11 == 0) <= (x&A != 0)) != 1:
#             Flag =0
#     if Flag == 1:
#         print(A)
#         break
