from collections import deque


def solv(merge_loc, visited, start):
    queue = deque([start])
    visited[start] = 1

    while queue:
        node = queue.popleft()

        for i in merge_loc[node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


# 출력은 제대로 되는데 틀림..다시 풀어보기. 순열을 sort해서 사용하면 안될것같음

res = []
for i in range(int(input())):
    N = int(input())

    merge_loc = [[] for _ in range(N+1)]
    visited = [0 for _ in range(N+1)]

    origin_number = list(map(int, input().split()))
    sequence_number = sorted(origin_number)
    count = 0

    for i in range(N):
        i, j = sequence_number[i], origin_number[i]
        merge_loc[i].append(j)
        merge_loc[j].append(i)

    for i in range(1, N):
        if visited[i] == 0:
            solv(merge_loc, visited, i)
            count += 1
    res.append(count)

for i in res:
    print(i)
