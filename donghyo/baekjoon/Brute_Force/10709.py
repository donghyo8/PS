if __name__ == "__main__":
    H, W = map(int, input().split())
    S = [list(str(input())) for _ in range(H)]
    C = [[0] * W for _ in range(H)]
    state = False

    for i in range(H):
        for j in range(W):
            if S[i][j] == '.' and not state:
                C[i][j] = -1
            elif S[i][j] == 'c':
                state = True
                C[i][j] = 0
                minutes = 1
            elif S[i][j] == '.' and state:
                C[i][j] = minutes
                minutes += 1
        state = False
        minutes = 1
    
    for i in C:
        print(" ".join(map(str, i)))
