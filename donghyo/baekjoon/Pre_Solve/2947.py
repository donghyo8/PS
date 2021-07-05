def solution(piece):
    temp = 0

    for i in range(len(piece)-1):
        if piece[i] > piece[i+1]:
            temp = piece[i+1]
            piece[i+1] = piece[i]
            piece[i] = temp
            print(' '.join((map(str, piece))))

piece = list(map(int, input().split()))

for i in piece:
    if i >= 1 and i <= 5 and len(piece) == len((set(piece))):
        if (list(set(piece)) != piece):
            solution(piece)
        else:
            break

    else:
        print("중복")
        break

