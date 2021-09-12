N = int(input())
player_list = [list(map(str, input())) for _ in range(N)]

dic = {}
for i in player_list:
    if i[0] in dic:
        dic[i[0]] += 1
    else:
        dic[i[0]] = 1

res = ''
for i, j in zip(dic.keys(), dic.values()):
    if j >= 5:
        res += i

if res:
    res = sorted(res)
    print("".join(res))
else:
    print('PREDAJA')
