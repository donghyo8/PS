def solution(arr1, arr2):
    answer = []
    temp = list()

    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            temp.append(arr1[i][j] + arr2[i][j])
        answer.append(temp)
        temp = []
    print(answer)
    return answer

solution([[1,2],[2,3]], [[3,4],[5,6]])