def main():
    N = int(input())
    wordList = list()

    for _ in range(N):
        wordList.append(str(input()))

    newList = set(wordList)
    newList = list(newList)

    newList.sort()
    newList.sort(key = lambda x:len(x))

    for i in newList:
        print(i)
 
main()