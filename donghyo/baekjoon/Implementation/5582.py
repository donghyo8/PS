A = str(input())
B = str(input())

# 시간초과남 DP로 풀기
res = 0
for i in range(len(B)):
    for j in range(i+1, len(B) + 1):
        if A.find(B[i:j]) >= 0:
            res = max(res, len(B[i:j]))
print(res)
