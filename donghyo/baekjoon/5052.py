def solution(numberList):
    numberList.sort()
    result = "YES"

    for i, j in zip(numberList, numberList[1:]):
        if i == j[:len(i)]:
            result = "NO"
    
    return result


def main():
    t = int(input())
    numberList = list()

    for i in range(t):
        n = int(input())

        for i in range(n):
            numberList.append(list(map(int, input())))
    
        result = solution(numberList)   
        print(result)
        numberList.clear()
            
main()