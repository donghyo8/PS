def solution():
    resultList = []
    N = int(input())

    infoList = [list(map(int, input().split())) for _ in range(N)]

    for i in infoList:
        rank = 1
        for j in infoList:
            if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    
        print(rank, end = " ")

solution()