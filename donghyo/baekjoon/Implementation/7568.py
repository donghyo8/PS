if __name__ == "__main__":
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in arr:
        rank = 1
        for j in arr:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
        
        print(rank, end = " ")