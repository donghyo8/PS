def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True

def dfs(x):
    global res

    if x == N:
        # print(row)
        res += 1 # 모든 열을 다 말을 놓을 수 있는 경우
    
    else:
        for i in range(N):
            row[x] = i

            if check(x):
                dfs(x + 1)

if __name__ == "__main__":
    N = int(input())
    row = [0] * N
    res = 0

    dfs(0)
    print(res)