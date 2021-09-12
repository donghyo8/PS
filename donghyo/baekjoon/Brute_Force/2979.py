if __name__ == "__main__":
    A, B, C = map(int, input().split())
    truck = [list(map(int, input().split())) for _ in range(3)]
    
    max_value = truck[0][1]
    for i in range(1, len(truck)):
        if max_value < truck[i][1]:
            max_value = truck[i][1]
    
    cost = 0
    for i in range(1, max_value + 1):
        cnt = 0
        if truck[0][0] < i <= truck[0][1]:
            cnt += 1
        if truck[1][0] < i <= truck[1][1]:
            cnt += 1
        if truck[2][0] < i <= truck[2][1]:
            cnt += 1

        if cnt == 1:
            cost += A * cnt
        elif cnt == 2:
            cost += B * cnt
        else:
            cost += C * cnt
    
    print(cost)