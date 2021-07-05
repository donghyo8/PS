from collections import deque

def func(NList):
    sortList = sorted(NList, key = lambda x:x[0])
    max = sortList[0][1]
    count = 1

    for i in range(1, len(sortList)):
        if max > sortList[i][1]:
            count += 1
            max = sortList[i][1]

    return count

def main():
    T = int(input())
    result = 0

    for i in range(T):
        N = int(input())
        nList =[list(map(int, input().split())) for _ in range(N)]
        result = func(nList)
        print(result)
        
main()