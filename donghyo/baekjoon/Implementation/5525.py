if __name__ == "__main__":
    N = int(input())
    S_length = int(input())
    S = list(str(input()))

    check = list('IOI')
    if N > 1:
        for i in range(2, N+1):
            check.append('O'), check.append('I')
       
    cnt = 0
    for idx, token_1 in enumerate(S):
        if token_1 == 'I':
            valid_1 = "".join(S[idx:idx+len(check)])
            valid_2 = "".join(check)
            if valid_1 == valid_2:
                cnt += 1

    print(cnt)


