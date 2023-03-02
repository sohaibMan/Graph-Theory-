infinity = float('inf')
A = [[0, 3, infinity, 7], [8, 0, 2, infinity], [
    5, infinity, 0, 1], [2, infinity, infinity, 0]]
n = len(A)
for k in range(n):
    for i in range(n):
        for j in range(n):
            A[i][j] = min(A[i][j], A[i][k]+A[k][j])

print(A)
