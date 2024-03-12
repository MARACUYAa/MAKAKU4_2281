s = open('24numb/24_demo.txt').read()[:-1]
s =s.replace('XX', 'A').replace('YY','B').replace('ZZ','C')
s =s.replace('AX', '*').replace('BY','*').replace('CZ','*')
s =s.replace('A', '*').replace('B','*').replace('C','*')
a = s.split('*')
a = list(map(len,a))
print( a[0], a[-1])
print(max(a)+2)