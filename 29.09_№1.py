x = int(input())
n = bin(x)[2:]
five = bin(5)[2:]
seven = bin(7)[2:]
if x % 5 == 0:
    n = n + five
else:
    n = n + '1'
if n % 7 == 0:
    n = n + seven
else:
    