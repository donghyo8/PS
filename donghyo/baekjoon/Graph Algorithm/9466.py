import sys
sys.setrecursionlimit(1000001)


def solv(start):
    global student_number, visited, node_path, res
    visited[start] = 1
    node_path.append(start)
    next_node = student_number[start]

    if visited[next_node] == 0:
        solv(next_node)
    else:
        if next_node in node_path:
            res += node_path[node_path.index(next_node):]


for i in range(int(input())):
    n = int(input())
    student_number = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    res = []

    for i in range(1, n+1):
        if visited[i] == 0:
            node_path = []
            solv(i)

    print(n - len(res))
