if __name__ == "__main__":
    N = int(input())

    paper = [[0] * 101 for _ in range(101)]
    for _ in range(N):
        a, b = map(int, input().split())

        for i in range(a, a+10):
            for j in range(b, b+10):
                paper[i][j] = 1

    res = 0
    for i in paper:
       res += i.count(1)
    
    print(res)
