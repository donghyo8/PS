from collections import Counter

def main():
    S = str(input())
    countList = list()
    alphaList = list()

    frequency = Counter(S.upper())

    for i, j in frequency.items():
        alphaList.append(i)
        countList.append(j)

    validCount = max(countList)

    if countList.count(validCount) > 1:
        print("?")
    else:
        for i in range(len(countList)):
            if validCount == countList[i]:
                print(alphaList[i])

main()