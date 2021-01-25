
def solution(s):
    stack = list()

    for i in s:
        # stack이 비어있을 경우 push
        if len(stack) == 0:
            stack.append(i)

        # stack top에 들어가있는 문자와 들어가려는 문자가 같으면 top pop
        elif stack[-1] == i:
            stack.pop()

        # 이전 문자가 같지않을 경우 push
        else:
            stack.append(i)

        print(stack)

    # 루프를 다돌고 stack에 아무것도 업으면 모두 제거할 수 있으므로 1 return
    if len(stack) == 0:
        return 1
    # 아닐경우 0 return
    else:
        return 0


s1 = "baabaa"
s2 = "cdcd"
solution(s2)