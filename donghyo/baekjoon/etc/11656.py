S = str(input())
arr = []

for i in range(len(S)):
    arr.append(S[i:len(S)])

arr.sort()

for i in arr:
    print(i)
