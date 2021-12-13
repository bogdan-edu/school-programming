graph = [0, 0, 0, 0, 0, 0]

graph[0] = [0, 1, 0, 0, 1, 0]
graph[1] = [1, 0, 1, 0, 1, 0]
graph[2] = [0, 1, 0, 1, 0, 0]
graph[3] = [0, 0, 1, 0, 1, 1]
graph[4] = [1, 1, 0, 1, 0, 0]
graph[5] = [0, 0, 0, 1, 0, 0]

# print(graph[3-1][4-1])

for row in range(len(graph)):
    print(graph[row])