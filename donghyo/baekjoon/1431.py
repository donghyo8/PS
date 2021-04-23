def solution():
    N = int(input())
    serial_Number = [list(map(str, input())) for _ in range (N)]

    # 1. 사전순, 2. 길이, 3. 숫자의 모든 자리수 합
    serial_Number.sort()
    serial_Number.sort(key = lambda x:(len(x), sum(int(i) for i in x if i.isnumeric())))

    for i in serial_Number:
        print("".join(i))
solution()