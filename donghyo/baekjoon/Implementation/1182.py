from itertools import combinations

def solv(N, S, arr):
    global res
    for i in range(1, N+1):
        comb = list(combinations(arr, i))
    
        for j in comb:
            if sum(j) == S:
                res += 1

if __name__ == "__main__":
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    res = 0
    solv(N, S, arr)
    print(res)