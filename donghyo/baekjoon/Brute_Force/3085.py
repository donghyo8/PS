def eat(arr):
    max_value = 0

    for i in range(len(arr)):
        first_res, second_res = 1, 1

        for j in range(len(arr)-1):
            if arr[i][j] == arr[i][j+1]:
                first_res += 1
            else:
                max_value = max(max_value, first_res)
                first_res = 1
            
            if arr[j][i] == arr[j+1][i]:
                second_res += 1
            else:
                max_value = max(max_value, second_res)
                second_res = 1
        max_value = max(max_value, first_res, second_res)

    return max_value

def change_first(arr, i, j):
    temp = arr[i][j]
    arr[i][j] = arr[i][j+1]
    arr[i][j+1] = temp
    return arr


def change_second(arr, i, j):
    temp = arr[j][i]
    arr[j][i] = arr[j+1][i]
    arr[j+1][i] = temp
    return arr


N = int(input())
arr = [list(map(str, input())) for _ in range(N)]

res = 0
for i in range(len(arr)):
    for j in range(len(arr[i])-1):
        if arr[i][j] != arr[i][j+1]:
            arr = change_first(arr, i, j)
            res = max(res, eat(arr))
            arr = change_first(arr, i, j)
        

        if arr[j][i] != arr[j+1][i]:
            arr = change_second(arr, i, j)
            res = max(res, eat(arr))
            arr = change_second(arr, i, j)

print(res)


        
