import sys

S = str(input())
M = int(input())
current_cursor = len(S)
arr = []

for i in S:
    arr.append(i)

# 시간초과남.. 시간제한(0.3초) , 다른 로직으로 다시 작성(삽입/제거 했을 때 앞뒤 원소를 건드릴필요가 없도록 작성해야할듯)
for i in range(M):
    command = sys.stdin.readline().strip()
    go = command.split(" ")

    if go[0] == 'P':
        arr.insert(current_cursor, go[1])
        current_cursor += 1
    elif go[0] == 'L':
        if current_cursor <= 0:
            current_cursor = 0
        else:
            current_cursor -= 1
    elif go[0] == 'D':
        current_cursor += 1
    elif go[0] == 'B':
        if current_cursor == 0:
            continue
        del arr[current_cursor-1]
        current_cursor -= 1

for i in arr:
    print(i, end="")
