from collections import deque
N = int(input())
res = 0

for i in range(N):
    word = str(input())
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                res += 1
                break

print(N - res)

    
