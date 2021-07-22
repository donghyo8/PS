from itertools import permutations
N = int(input())

temp = []
for i in range(1, 10): temp.append(i)
permu = list(permutations(temp, 3))

for _ in range(N):
    number, st, ba = map(int, input().split())
    spli = list(str(number))
    remove_idx = 0

    for i in range(len(permu)):
        i -= remove_idx
        st_count, ba_count = 0, 0

        for j in range(3):
            if int(spli[j]) in permu[i]: 
                if j == permu[i].index(int(spli[j])): # strike
                    st_count += 1
                else:  # ball
                    ba_count += 1 

        if (st_count != st) or (ba_count != ba):
            permu.remove(permu[i])
            remove_idx += 1

print(len(permu))
