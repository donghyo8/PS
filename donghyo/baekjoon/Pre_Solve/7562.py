from collections import deque

def bfs(start_x, start_y, end_x, end_y, length, matrix):
    validx = [-2, -1, 1, 2, 2, 1, -1, -2]
    validy = [1, 2, 2, 1, -1, -2, -2, -1]
    
    count = 0
    queue = deque()
    queue.append([start_x, start_y, 0])

    if start_x == end_x and start_y == end_y:
        return 0

    while queue:
        x, y, count = queue.popleft()

        for i in range(len(validx)):
            check_x, check_y = x + validx[i], y + validy[i]

            if 0 <= check_x < length and 0 <= check_y < length and matrix[check_x][check_y] == 0:
                matrix[check_x][check_y] = 1
                if check_x == end_x and check_y == end_y:
                    return count + 1
                else:
                    queue.append([check_x,check_y, count + 1])

def main():
    T = int(input())
    
    for _ in range(T):
        length = int(input())
        start_x, start_y = list(map(int, input().split()))
        end_x, end_y = list(map(int, input().split()))
        matrix = [[0] * length for _ in range(length)]

        print(bfs(start_x, start_y, end_x, end_y, length, matrix))

main()