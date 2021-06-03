# 투포인터

N, M = map(int, input().split())
A = list(map(int, input().split()))

sum = start = end = count = 0

while start >= N:

    while sum < M and end < N:
        sum += A[end]
        end += 1

    # start와 end의 부분합이 M이랑 같으면 카운트를 증가하고 start 인덱스 증가
    if sum == M:
        count += 1
    
    sum -= A[start]
    start += 1

print(count)