from collections import deque

def validWord(top, prev):
    answer = 0

    for i in range(len(top)):
        if top[i] != prev[i]:
            answer += 1
            if answer == 2:
                return False
    if answer == 1:
        return True
    return False

def solution(begin, target, words):
    stack = deque([begin])
    visited = list() 
    answer = 0  

    if target not in words:
        return 0 

    while stack:
        top = stack.pop()

        if top == target:
            print(answer)
            return answer
        else:
            for i in range(len(words)):
                if words[i] not in visited:
                    # print(top, words[i], validWord(top, words[i]))
                    if validWord(top, words[i]):
                        stack.append(words[i])
                        visited.append(words[i])
        answer += 1

    print(answer)
    return answer

words1 = ["hot", "dot", "dog", "lot", "log", "cog"]
words2 = ["hot", "dot", "dog", "lot", "log"]
solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"])
