def main():
    n = int(input())
    tri = list()
    
    for _ in range(n):
        tri.append(list(map(int, input().split())))

    for i in range(1, len(tri)):
        for j in range(len(tri[i])):
            if j == 0:
                tri[i][j] += tri[i-1][j]
            elif i == j:
                tri[i][j] += tri[i-1][j-1]
            else:
                tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])

    print(max(tri[-1]))

main()