from collections import Counter

N = int(input())
book_title = [str(input()) for _ in range(N)]

counter = Counter(book_title)
arr = counter.most_common()

max_value = 0
res = []
for i in arr:
    if i[1] >= max_value:
        max_value = i[1]
        res.append(i[0])

res.sort()
print(res[0])