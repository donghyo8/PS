def main():
    K = int(input())
    integerList = list()

    for _ in range(K):
        integerList.append(int(input()))

        if integerList[-1] == 0:
            integerList.pop()
            integerList.pop()

    if integerList:
        print(sum(integerList))
    else:
        print(0)
          
main()