T = int(input())
res = []

for _ in range(T):
    text = str(input())
    left, right = [], []

    for i in text:
        if i == "<":
            if left:
                right.append(left.pop())

        elif i == ">":
            if right:
                left.append(right.pop())

        elif i == "-":
            if left:
                left.pop()

        else:
            left.append(i)

        print(left, right)

    res.append("".join(left)+"".join(reversed(right)))

for i in res:
    print(i)
