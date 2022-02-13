import sys

def dfs(x, y, token):
    global res
    valid_x, valid_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    state = 0
    
    for i in range(4):
        check_x, check_y = x + valid_x[i], y + valid_y[i]

        if 0 <= check_x < R and 0 <= check_y < C and matrix[check_x][check_y] not in token:
            dfs(check_x, check_y, token + matrix[check_x][check_y])
        else:
            state += 1
    
    if state == 4:
        res = max(res, len(token))
        print(token, state)
        return

if __name__ == "__main__":
    R, C = map(int, input().split())
    matrix = [list(sys.stdin.readline().strip()) for _ in range(R)]
    res = 0
    dfs(0, 0, matrix[0][0])
    print(res)

