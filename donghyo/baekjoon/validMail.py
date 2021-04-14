from collections import deque

def solution(mails):
    answer = 0
    front = deque()
    stack = deque()
    j = 0
    check = [".com", ".net", ".org"]

    for i in mails:
        if i[-4:] in check:
            front.append(list(i[:-4]))
    
    print(front)
    for i in range(len(front)):
        j = 0
        
        while True:
            if len(front[i]) - 1 == j:
                stack.clear()
                break
            if front[i][j] == "@":
                if "@" not in stack:
                    stack.append(front[i][j])
                    answer += 1
                else:
                    stack.pop()
                    answer -= 1
            j += 1

    print(answer)
    return answer


email1 = ["d@co@m.com", "a@abc.com", "b@def.com", "c@ghi.net"]
email2 = ["abc.def@x.com", "abc", "abc@defx", "abc@defx.xyz"]
solution(email1)