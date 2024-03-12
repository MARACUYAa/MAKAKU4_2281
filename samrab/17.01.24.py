import ipaddress
from ipaddress import *
# net = ip_network('129.128.0.0/255.128.0.0',0)
# print(f'{net[0]:b}')
#2
# net = ip_network('185.8.0.0/255.255.128.0',0)
# print(f'{net[-1]:b}'.count('1'))
# #3
# for a in range(256):
#     net = ip_network(f'223.167.{a}.167/255.255.255.192',0)
#     flag = 1
#     for i in net:
#         b = f'{i:b}'
#         if b[:16].count('0') > b[-16:].count('0'):
#             flag = 0
#     if flag == 1:
#         print(a)
# #4
# k = 0
# net = ip_network('165.44.96.0/255.255.248.0',0)
# for i in net:
#     b = f'{i:b}'
#     if '111' in b:
#         k+=1
# print(k)
# #5
# for i in range(33):
#     mask = ip_network(f'173.103.25.118/{i}', 0)
#     print(mask, 32-i)
# #6
# for i in range(33):
#     mask = ip_network(f'154.201.208.17/{i}', 0)
#     print(mask.netmask, mask)
# #7
# for i in range(33):
#     net = ip_network(f'108.133.75.91/{i}', 0)
#     print(net, net.num_addresses)
# #8
# for i in range(33):
#     net = ip_network(f'175.122.80.13/{i}', 0)
#     print(net, net.netmask, net.num_addresses)
for mask in range(16, 33):
    net = ip_network(f'187.124.21.237/{mask}', 0)
    flag = 1
    for x in net:
        b = f'{x:b}'
        if b[:16].count('1') < b[-16:].count('1'):
            flag = 0
    if flag == 1:
        print(net, net.netmask)

