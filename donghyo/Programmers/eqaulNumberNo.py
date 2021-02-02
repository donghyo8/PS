def solution(arr):
    answer = []
    # temp = arr[0]
    answer.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])

        # if temp == arr[i]:
        #     if len(answer) <= 0:
        #         answer.append(temp)

        #     elif str(answer[-1]) not in str(temp): 
        #         answer.append(temp)  

        # elif str(answer[-1]) not in str(temp):
        #     answer.append(temp)
        # temp = arr[i]

    print(answer)    
    return answer

solution([4,4,4,3,3])