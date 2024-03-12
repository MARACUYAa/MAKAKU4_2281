M = []
for i in range(251,1000):
    s = i * '5'
    s1 = s
    while '55555' in s:
        s= s.replace('55555', '88', 1)
        s = s.replace('888', '555', 1)
    s = s.replace('8', '')
    M.append(int(s))
    if s == '5':
        print(len(s1))
        break
