import sys
from collections import Counter

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(N)]
    arr.sort()
    a = round(sum(arr) / N)
    b = arr[int(N / 2)]

    temp = Counter(arr).most_common()
    c = 0

    if len(temp) == 1:
        c = temp[0][0]
    elif temp[0][1] == temp[1][1]:
        c = temp[1][0]
    else:
        c = temp[0][0]

    print(a)
    print(b)
    print(c)
    print(arr[-1] - arr[0])