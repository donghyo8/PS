T = str(input())
arr = [0] * 26

for i in T:
    arr[ord(i) - 97] += 1

for i in arr:
    print(i, end=" ")
