import sys

def solv(arr):
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1][0:len(arr[i])]:
            return "NO"
    return "YES"


res = []
for i in range(int(input())):
    n = int(input())
    arr = [sys.stdin.readline().strip() for _ in range(n)]
    arr.sort()
    res.append(solv(arr))

for i in res:
    print(i)


