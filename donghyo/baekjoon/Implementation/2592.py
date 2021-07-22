from collections import Counter

arr = [int(input()) for _ in range(10)]
c =Counter(arr).most_common()

print(sum(arr) // len(arr))
print(c[0][0])
