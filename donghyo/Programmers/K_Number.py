def solution(array, commands):
    answer = []

    for number in commands:
        select_idx = number[2]
        arr = sorted(array[number[0]-1:number[1]])
        answer.append(arr[select_idx - 1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
solution(array, commands)
