adj_list = {
    "A": [["B", 28], ["F", 10]],
    "B": [["A", 28], ["G", 14], ["C", 16]],
    "C": [["D", 12], ["B", 16]],
    "D": [["C", 12], ["E", 22], ["F", 18]],
    "E": [["F", 25], ["D", 22], ["G", 24]],
    "F": [["A", 10], ["E", 25]],
}
out_tree = {}
min = 0
vertex = []  # couple
for u in adj_list:
    print(u)
    for n in adj_list[u]:
        if min > n[1]:
            min = n[1]
            vertex = [u, n[0], min]

print(vertex)
