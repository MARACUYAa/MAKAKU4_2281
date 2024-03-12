Gr = {1: [3],
      2: [3,4],
      3: [1,2,5],
      4: [2],
      5: [3]}

def poisk(ver, k):
    global a
    a[ver] = k
    vis.add(ver)
    for neir in Gr[ver]:
        if neir not in vis:
            poisk(neir, k+1)


res = {}
for start in Gr:
    a = {}
    vis = set()
    poisk(start, 0)
    res[start] = a
for k,v in res.items():
    print(  k + ':' + v)