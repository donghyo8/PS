def main():
    N, L = map(int,input().split())
    location = list(map(int,input().split()))
    result = 0
    valid = 0
    location.sort()

    for i in location:
        if valid < i:
            result += 1
            valid = i + L - 1

    print(result)
main()

