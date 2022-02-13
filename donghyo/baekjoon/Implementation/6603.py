from itertools import combinations

def solv(K, S):
    comb = list(combinations(S, 6))

    for i in comb:
        print(' '.join(map(str, i)))


if __name__== "__main__":
    while True:
       K, *S = list(map(int, input().split()))

       if K == 0:
           exit()

       solv(K, S)
       print()
       