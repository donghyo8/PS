def main():
    # 1~4번의 이동 제약조건이 항상 오른쪽으로 이동함
    N, M = map(int, input().split())

    if N == 1:
        print(1)

    elif N == 2:
        print(min(4, (M + 1) // 2))
    
    else:
        if M <= 6:
            print(min(4, M))
        else:
            print(M-2)

    # 비슷한 문제를 또 풀시 햇갈리지 말것. 보자마자 탐색하려고 생각했는데 그런 의도의 문제가 아니었음

    # matrix = [[0] * N for _ in range(M)]
    # matrix[M-1][0] = 1
    # 1. [i-2][j], [i][j+1]
    # 2. [i-1][j], [i][j+2]
    # 3. [i+1][j], [i][j+2]
    # 4. [i+2][j], [i][j+1]


main()