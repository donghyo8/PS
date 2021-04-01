def main():
    S = str(input())
    strList = [] * len(S)

    for i in range(len(S)):
        strList.append(S[i:len(S)])

    result = sorted(strList)

    for i in result:
        print(i)

main()