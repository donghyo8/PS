N = int(input())
A = list(map(int, input().split()))
M = int(input())
target_num_list = list(map(int, input().split()))
A.sort()

for idx in range(len(target_num_list)):
    left, right = 0, len(A) - 1
    flag = False

    while left <= right:
        mid = (left + right) // 2

        if A[mid] == target_num_list[idx]:
            print(1)
            flag = True
            break

        elif A[mid] > target_num_list[idx]:
            right = mid - 1
        else:
            left = mid + 1

    if not flag:
        print(0)
