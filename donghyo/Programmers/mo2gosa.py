from collections import deque
def solution(answers):
    answer = []
    first_Student = [1, 2, 3, 4, 5]
    second_Student = [2, 1, 2, 3, 2, 4, 2, 5]
    third_Student = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0] * 3

    for i in range(len(answers)):
        if answers[i] == first_Student[i % 5]:
            score[0] += 1
        if answers[i] == second_Student[i % 8]:
            score[1] += 1
        if answers[i] == third_Student[i % 10]:
            score[2] += 1

    max_Student = max(score[0], score[1], score[2])

    for i in range(3):
        if score[i] == max_Student:
            answer.append(i+1)

    print(answer)
    return answer

solution([1,3,2,4,2])