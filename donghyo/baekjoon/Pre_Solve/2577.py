def main():
    validList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    A, B, C = int(input()), int(input()), int(input())
    resultList = list()
    mul = A * B * C

    for i in validList:
        sum = 0
        for j in str(mul):
            if i == j:
                sum += 1
        resultList.append(sum)

    for i in resultList:
        print(i)
      
main()