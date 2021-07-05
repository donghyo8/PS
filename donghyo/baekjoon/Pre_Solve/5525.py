count = 0
result = 0
idx = 0
state = False

N = int(input())
M = int(input())
S = str(input())

while True:
    if idx == M-1:
        break

    if S[idx-1] == 'I' and S[idx] == 'O' and S[idx+1] == 'I':
        # print(idx-1, idx, idx+1, M-1)
        count += 1
        state = True
    else:
        state = False

    if state:
        idx += 2
    else:
        idx += 1

print(count)