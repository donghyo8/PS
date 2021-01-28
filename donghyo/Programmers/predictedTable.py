def solution(n,a,b):
    answer = 0
    # candidateList = list()

    # for i in range(1, n + 1):
    #     candidateList.append(i)
    # print(candidateList)

    # while n:
    #     if len(candidateList) == 1:
    #         break

    #     n = n // 2
        
    #     for i in range(n):
    #         candidateList.pop()


    #     print(candidateList)

    # a != b, N 이하 자연수
    
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2

        answer += 1

    print(answer)       
    return answer

solution(8, 4, 7)