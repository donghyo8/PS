N, M = map(int, input().split())
seq_list = []

def dfs():
    if len(seq_list) == M:
        print(' '.join(map(str, seq_list)))

    for i in range(1, N+1):
        if i not in seq_list:
            seq_list.append(i)
            dfs()
            seq_list.pop()
dfs()