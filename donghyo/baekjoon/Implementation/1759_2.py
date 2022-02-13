def solv(depth, idx):
    if depth == L:
        all_out.append("".join(map(str, out)))

    for i in range(idx, C):
        out.append(arr[i])
        solv(depth+1, i+1)
        out.pop()

def check(list_check):
    mo = 'aeiou'
    global res
    for i in list_check:
        mo_cnt, ja_cnt = 0, 0
        for j in i:
            if j in mo:
                mo_cnt += 1
            else:
                ja_cnt += 1
        if mo_cnt >= 1 and ja_cnt >= 2:
            res.append("".join(i))

if __name__ == "__main__":
    out, all_out, res = [], [], []
    L, C = map(int, input().split())
    arr = sorted(list(map(str, input().split())))
    print(arr)
    solv(0, 0)
    check(all_out)

    for i in res:
        print(i)
    