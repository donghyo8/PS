N = int(input())
arr = []
dic = {}

for i in range(N):
    arr.append(int(input()))

for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

res = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(res[0][0])
