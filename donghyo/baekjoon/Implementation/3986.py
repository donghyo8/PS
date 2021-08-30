N = int(input())
arr = [list(input()) for _ in range(N)]

count = 0
for a in arr:
    stack = []
    for idx in range(len(a)):
        if not stack:
            stack.append(a[idx])
        else:
            if stack[-1] == a[idx]:
                stack.pop()
            else:
                stack.append(a[idx])
    
    if not stack:
        count += 1
print(count)