M, N = map(int, input().split())


def solve(number):
    if number == 1:
        return False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False

        return True


for number in range(M, N+1):
    if solve(number):
        print(number)
