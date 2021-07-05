s = input()
stack = []
count = 0

for idx, token in enumerate(s):
    if token == "(":
        stack.append(token)
    elif token == ")" and s[idx-1] == "(":
        stack.pop()
        count += len(stack)
    
    elif token == ")":
        stack.pop()
        count += 1

print(count)
