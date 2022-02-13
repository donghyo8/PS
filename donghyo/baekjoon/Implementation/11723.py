import sys

if __name__ == "__main__":
    M = int(input())
    S = set()

    for _ in range(M):
        temp = sys.stdin.readline().strip().split()

        if len(temp) == 1:
            command = temp[0]
        else:
            command, x = temp[0], int(temp[1])


        if command == 'add':
            S.add(x)
        elif command == 'remove':
            S.discard(x)
        elif command == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)
        elif command == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif command == 'all':
            S = list(range(1, 21))
        else:
            S = set()
    