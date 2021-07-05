N, M = map(int, input().split())
number = list(map(int, input().split()))
sum = 0
sum_list = [0]

for i in number:
    sum += i
    sum_list.append(sum)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i-1])