def solution(A,B):
    answer = 0

    A = sorted(A)
    B = sorted(B, reverse=True)
    print(A)
    print(B)

    answer = sum([a * b for a, b in zip(A, B)])

    print(answer)
    return answer

A1 = [1, 4, 2]
B1 = [4, 5, 4]
A2 = [1,2]
B2 = [3,4]
solution(A1, B1)