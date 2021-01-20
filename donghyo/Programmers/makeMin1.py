def solution(A,B):
    answer = 0
    i = 1

    while(A):
        if A == '':
            break
        
        if i == len(B):
            i = 0

        temp = A[0]
        answer += temp * B[i]
        A.pop(0)
        i += 1
        
        print(answer)
    return answer

A1 = [1, 4, 2]
B1 = [4, 5, 4]
A2 = [1,2]
B2 = [3,4]
solution(A1, B1)