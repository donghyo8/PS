N = int(input())
score = []

for i in range(N):
   score.append(int(input()))

temp = count = 0
score.reverse()
temp = score[0]

for idx in range(1, len(score)):
    while temp <= score[idx]:
        score[idx] -= 1
        count += 1

    temp = score[idx]

print(count)  