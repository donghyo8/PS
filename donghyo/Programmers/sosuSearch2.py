def solution(n):
    answer = 0

    temp = [False, False] + [True] * n
    print (temp)
    primes = []

    for i in range(2, n + 1):
        if temp[i]:
            primes.append(i)
            for j in range(2 * i, n + 1, i):
                temp[j] = False

    answer  = primes
    print(len(answer))
    return len(answer)

n = 5
solution(n)

