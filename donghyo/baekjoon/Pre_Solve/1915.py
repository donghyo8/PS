def main():
    n, m = map(int, input().split())
    matrix =[list(map(int, input())) for _ in range(n)]
    result = 0

    # 4칸씩 한덩어리 체크(대각, 좌우) 0이라도 하나껴있으면 해당 덩어리는 정사각형 X
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 1:
                matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
    print(matrix)

    for i in matrix:
        result = max(result, max(i))

    print(result **2)

main()