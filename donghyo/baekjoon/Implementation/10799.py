brackets = str(input())
stack = []
res = 0

for idx, token in enumerate(brackets):
    if token == "(":
        stack.append(token)
    else:
        if brackets[idx-1] == "(":
            stack.pop()
            res += len(stack)
        else:
            stack.pop()
            res += 1

print(res)
