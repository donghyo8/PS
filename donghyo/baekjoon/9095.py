def call(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return call(n-1) + call(n-2) + call(n-3)

def main():
    T = int(input())

    for _ in range(T):
        n = int(input())
        print(call(n))
main()