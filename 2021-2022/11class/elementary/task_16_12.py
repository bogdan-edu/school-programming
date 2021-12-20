graph = [0, 0, 0, 0, 0, 0]

graph[0] = [0, 1, 0, 0, 1, 0]
graph[1] = [1, 0, 1, 0, 1, 0]
graph[2] = [0, 1, 0, 1, 0, 0]
graph[3] = [0, 0, 1, 0, 1, 1]
graph[4] = [1, 1, 0, 1, 0, 0]
graph[5] = [0, 0, 0, 1, 0, 0]

for row in range(len(graph)):
    print(graph[row])

node = int(input('Для якої вершини треба порахувати звʼязки? '))

relations = 0
for el in graph[node]:
    relations += el

print(f'Вершина {node} має {relations} звʼязків')