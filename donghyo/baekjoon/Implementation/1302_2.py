from collections import Counter
N = int(input())

dic = {}
arr = [str(input()) for _ in range(N)]
counter = Counter(arr)
cnt = counter.most_common()

max_value = 0
res = []
for i in cnt:
    if max_value <= i[1]:
        max_value = i[1]
        res.append(i[0])
        max_key = i[0]

res.sort()
print(res[0])