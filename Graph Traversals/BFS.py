# Description: Graph Traversals
from queue import Queue
adj_list = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B'],
    'D': ['A', 'E', 'F'],
    'E': ['D', 'F', 'G'],
    'F': ['D', 'H', 'E'],
    'G': ['E', 'H'],
    'H': ['F', 'G']
}
q = Queue()
out_list = []
visited = {}
for key in adj_list.keys():
    visited[key] = False


def BFS(u):
    q.put(u)
    while not q.empty():
        v = q.get()
        out_list.append(v)
        for n in adj_list[v]:
            if not visited[n]:
                visited[n] = True
                q.put(n)


BFS('A')
print(out_list)
