def main():
    N = int(input())

    result = sorted(str(N), reverse= True)

    print("".join(result))

main()