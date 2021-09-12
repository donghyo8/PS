if __name__ == "__main__":
    S = list(str(input()))

    res = ''
    for token in S:
        if 'a' <= token <= 'z':
            if token <= 'm': # 13
                res += chr(ord(token) + 13)
            else:
                res += chr(ord(token) - 13)

        elif 'A' <= token <= 'Z':
            if token <= 'M': # 13
                res += chr(ord(token) + 13)
            else:
                res += chr(ord(token) - 13)
        else:
            res += token
    print(res)

    