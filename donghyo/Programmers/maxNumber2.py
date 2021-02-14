# from itertools import permutations

def solution(numbers):
    answer = ''
    tempList = list()

    for i in numbers:
        tempList.append(str(i))
    
    # tempList의 원소들을 3번씩 곱하고 비교해 내림차순 정렬
    # '1' = '111', '10' = '101010'
    # 앞에자리 부터 비교하여 큰 기준으로 정렬
    tempList.sort(key=lambda x : x*3, reverse=True)

    for i in tempList:
        answer += i

    print(tempList)
    print(answer)

    if answer[0] == '0':
        return '0'

    return answer

    # if len(numbers) >= 1:
    #     for i in numbers:
    #         tempList.append(str(i))
        
    #         combList = list(map(''.join, permutations(tempList)))
    #         answer =  max(combList)

    #     print(answer)
    #     return answer

solution([6, 10, 2])