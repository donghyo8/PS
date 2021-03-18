def main():
    dic1, dic2 = {}, {}
    N, M = map(int, input().split())

    for i in range(1, N+1):
       pocketmon_Name = str(input())
       if pocketmon_Name[0].isupper() and pocketmon_Name[1:].islower():
            dic1[i] = pocketmon_Name
            dic2[pocketmon_Name] = i

    for _ in range(M):
        what = str(input())
    if what.isdigit():
        print(dic1[int(what)])
    else:
        print(dic2[what])

main()