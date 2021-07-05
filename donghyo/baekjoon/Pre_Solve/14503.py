def leftTurn(index):
    if index == 0: 
        return 3
    elif index == 1:  
        return 0
    elif index == 2:
        return 1
    elif index == 3:
        return 2

def directionCheck(directionFlag, x, y, d, matrix):
    if directionFlag == 0:
        if d == 0:
            x += 1
        elif d == 1:
            y -= 1
        elif d == 2:
            x -= 1
        elif d == 3:
            y += 1

        if matrix[x][y] == 1: # 벽만나면 멈춤
            return x, y, True
    
    return x, y, False
    

def clean(matrix, r, c, d, N, M):
    valid_x, valid_y = [-1, 0, 1, 0], [0, 1, 0, -1]
    x, y = r, c
    matrix[x][y] = 2
    count = 1

    while True:
        direction = d

        for _ in range(4):
            direction = leftTurn(direction)
            check_x, check_y = x + valid_x[direction], y + valid_y[direction]
            directionFlag = 0

            if 0 <= check_x < N and 0 <= check_y < M and matrix[check_x][check_y] == 0:
                x, y, d = check_x, check_y, direction
                matrix[check_x][check_y] = 2
                count += 1
                directionFlag = 1
                break
        
        x, y, stopFlag = directionCheck(directionFlag, x, y, d, matrix)

        if stopFlag:
            break

    return count

def main():
    N, M = map(int, input().split())
    r, c, d = list(map(int, input().split()))
    matrix = [list(map(int , input().split())) for _ in range(N)]

    print(clean(matrix, r, c, d, N, M))

main()