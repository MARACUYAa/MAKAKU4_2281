#Ввод графа с клавиатуры
Gr = {}
rebra = set()
s = input()
while s != '':
    rebra.add(s)
    s = input()
print(rebra)
rebra -= {''}
Graph = {}
for rebro in rebra:
    a, b = rebro[0], rebro[1]
    if a not in Graph:
        Graph[a] = []
    Graph[a].append(b)

print(Graph)