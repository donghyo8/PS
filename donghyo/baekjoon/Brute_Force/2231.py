N = int(input())

for i in range(1, N+1):
    number = list(map(int, str(i)))
    answer = i + sum(number)

    if i == N:
        print(0)

    if answer == N:
        print(i)
        break
