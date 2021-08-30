def valid_check(bracket, idx):
    stack, res = [], []

    for token in bracket:
        if not stack:
            if token == '{':
                stack.append(token)
            else:
                continue
        else:
            if token == '}':
                stack.pop()
            else:
                stack.append(token)

    if not stack:
        res.append(str(idx) + ". " + '0')

    else:
        temp = change_bracket(bracket)
        res.append(str(idx) + ". " + str(temp))

    return res


def change_bracket(bracket):
    origin = ['{', '}']
    ans, idx = 0, 0

    print(bracket)
    for idx_1, token in enumerate(bracket):
        if token != origin[idx]:
            if bracket[idx_1] == '{':
                bracket[idx_1] = '}'
            else:
                bracket[idx_1] = '{'
            ans += 1
        idx += 1

        if idx == len(origin):
            idx = 0

    print(bracket)
    print(ans)
    return ans


if __name__ == "__main__":
    res = []
    idx = 1
    while True:
        bracket = list(str(input()))

        if "-" in bracket:
            break

        res.append(valid_check(bracket, idx))
        idx += 1

    for i in res:
        print("".join(i))
