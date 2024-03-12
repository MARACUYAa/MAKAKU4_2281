Graph = {'A': ['B'],
         'B': ['A', 'C', 'D'],
         'C': ['B', 'D'],
         'D': ['B', 'C']}

sv = {}
ver = 'C'
que = ['B', 'D']
vis = set()
while len(que) != 0:
    vis.add(ver)
    sv[ver] = 0
    for neir in Graph[ver]:
        if neir not in vis:
            que.append(neir)
print(sv)
