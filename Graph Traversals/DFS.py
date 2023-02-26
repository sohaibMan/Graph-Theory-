# python dictionary
adj_list = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["B", "F"],
    "D": [],
    "E": ["F"],
    "F": []

}
# DFS DEPTH FIRST SEARCH

dfs_output = []


def DFS(u):

    dfs_output.append(u)
    for v in adj_list[u]:
        if v not in dfs_output:
            DFS(v)


DFS("A")
print(dfs_output)
