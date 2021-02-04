def solution(arr):
    answer = []
    temp = min(arr)

    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(temp)

    answer = arr
    return answer

solution([10])