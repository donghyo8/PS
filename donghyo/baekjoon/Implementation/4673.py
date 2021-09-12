if __name__ == "__main__":
    origin_number = set(range(1, 10001))
    temp = set()
    for i in range(1, 10001):
        for j in str(i):
            i += int(j)
        temp.add(i)

    self_number = sorted(origin_number - temp)

    for i in self_number:
        print(i)