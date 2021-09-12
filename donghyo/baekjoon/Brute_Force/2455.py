if __name__ == "__main__":
    total = 0
    res = []
    for _ in range(4):
        a, b = map(int, input().split())
        total -= a
        total += b
        res.append(total)
    print(max(res))

        