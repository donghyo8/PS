from itertools import combinations

def solv(arr):
    global res

    mo = set(['a','e','i','o','u'])
    ja = set([i for i in arr if i not in mo])

    for word in list(combinations(arr, L)):
        mo_cnt, ja_cnt = 0, 0
        for token in word:
            if token in mo:
                mo_cnt += 1
            else:
                ja_cnt += 1
        if mo_cnt >= 1 and ja_cnt >= 2:
            res.append("".join(word))

    
if __name__ == "__main__":
    res = []
    L, C = map(int, input().split())
    arr = sorted(list(map(str, input().split())))
    solv(arr)

    for i in res:
        print(i)