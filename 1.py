from fnmatch import fnmatch

for x in range(0, 10 ** 8, 21):
    if fnmatch(str(x), '1234*54'):
        print(x, x // 21)
