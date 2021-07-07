import sys

S = str(input())
M = int(input())
# current_cursor = len(S)

stack1 = []
stack2 = []

for i in S:
    stack1.append(i)

for i in range(M):
    command = sys.stdin.readline().strip()
    go = command.split(" ")

    if go[0] == 'P':
        stack1.append(go[1])

    elif go[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
        else:
            continue
    elif go[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
        else:
            continue
    elif go[0] == 'B':
        if stack1:
            stack1.pop()
        else:
            continue

print("".join(stack1 + list(reversed(stack2))))

# if go[0] == 'P':
#     arr.insert(current_cursor, go[1])
#     current_cursor += 1
# elif go[0] == 'L':
#     if current_cursor <= 0:
#         current_cursor = 0
#     else:
#         current_cursor -= 1
# elif go[0] == 'D':
#     current_cursor += 1
# elif go[0] == 'B':
#     if current_cursor == 0:
#         continue
#     del arr[current_cursor-1]
#     current_cursor -= 1

# for i in arr:
#     print(i, end="")
