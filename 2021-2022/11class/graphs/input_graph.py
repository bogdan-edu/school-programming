graph = []

node_len = int(input('Ведіть кількість вершин графа: '))

for i in range(node_len):
    graph.append([])
    for j in range(node_len):
        relation = int(input(f'Чи має вершина {i + 1} звʼязок з вершиною {j + 1} (так - 1, ні - 0) : '))
        graph[i].append(relation)

for row in range(len(graph)):
    print(graph[row])

with open('files/graph.txt', 'a', encoding='utf-8') as file:
    file.write(f'{graph}\n')