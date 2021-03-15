def main():
    N = int(input())
    weight = list()
    resultList = list()

    for _ in range(N):
        weight.append(int(input()))

    weight.sort(reverse=True)

    for i in range(N):
        resultList.append(weight[i] * (i + 1))
    print(max(resultList))
       
main()