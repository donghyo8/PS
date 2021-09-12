from itertools import permutations

if __name__ == "__main__":
    N = int(input())
    arr = [i for i in range(1, N+1)]

    for i in list(permutations(arr)):
        for j in i:
            print(j, end = ' ')
        print()
