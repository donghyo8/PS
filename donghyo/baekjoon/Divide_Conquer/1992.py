def solv(x:int, y:int, N:int):
    global res
    check = quad_tree[x][y]

    for i in range(N):
        for j in range(N):
            if check != quad_tree[i+x][j+y]: # 4개중 하나라도 다르면 재귀
                res.append('(')
                solv(x, y, N//2) # 좌측상단
                solv(x, y+N//2, N//2) # 우측상단
                solv(x+N//2, y, N//2) # 좌측하단
                solv(x+N//2, y+N//2, N//2) # 우축하단
                res.append(')')
                return res
    res.append(check)


if __name__ == "__main__":
    res = []
    N = int(input())
    quad_tree = [list(map(int, input())) for _ in range(N)]
    solv(0, 0, N)
    print("".join(map(str, res)))

    