def main():
    temp = list()

    while True:
        data = list(map(int, input().split()))

        if data == [0, 0, 0]:
            break
        else:
            temp.append(data)

    for i, (L, P, V) in enumerate(temp):
        result = V // P * L

        if V % P >= L:
            result += L
        else:
            result += V % P
        
        print(f"Case {i+1}: {result}")

main()