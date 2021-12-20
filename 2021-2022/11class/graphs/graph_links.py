def show_graph(graph):
    for r in range(len(graph)):
        print(graph[r])


graph1 = [[2, 5],
          [1, 3, 5],
          [2, 4],
          [3, 5, 6],
          [1, 2, 4],
          [4]]

graph2 = [[0, 1, 0, 0, 1, 0],
          [1, 0, 1, 0, 1, 0],
          [0, 1, 0, 1, 0, 0],
          [0, 0, 1, 0, 1, 1],
          [1, 1, 0, 1, 0, 0],
          [0, 0, 0, 1, 0, 0]]

show_graph(graph1)

show_graph(graph2)
