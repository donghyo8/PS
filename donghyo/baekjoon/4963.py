from collections import deque

def search(i, j, matrix, w, h):
    valid_x, valid_y = [1,1,1,0,0,-1,-1,-1], [-1,0,1,-1,1,-1,0,1]

    queue = deque()
    queue.append([i, j])

    while queue:
        x, y = queue.popleft()
        
        for i in range(8):
            check_x, check_y = x + valid_x[i], y + valid_y[i]
            
            if 0 <= check_x < h and 0 <= check_y < w:
                if matrix[check_x][check_y] == 1:
                    matrix[check_x][check_y] = 0
                    queue.append([check_x, check_y])


def main():
    while True:
        w, h = map(int, input().split())

        if w == 0 and h == 0:
            break

        matrix = [list(map(int, input().split()))for _ in range(h)]
        count = 0

        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 1:
                    search(i, j, matrix, w, h)
                    count += 1
        print(count)
main()