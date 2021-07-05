T = int(input())


def valid_Bracet(brackets):
    stack = []

    for token in brackets:
        if not stack:
            if token == "(":
                stack.append(token)
            else:
                return "NO"
        else:
            if token == "(":
                stack.append(token)
            else:
                stack.pop()

    if len(stack) == 0:
        return "YES"

    return "NO"


res = []
for _ in range(T):
    brackets = str(input())
    res.append(valid_Bracet(brackets))

for i in res:
    print(i)
