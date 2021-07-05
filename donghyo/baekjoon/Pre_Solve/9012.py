from collections import deque

def validbracket(p):
    stack= deque()

    for i in p:
        if len(stack) == 0:
            if i=='(':
                stack.append(i)
            else: 
                return "NO"
        elif i == '(':
            stack.append(i)
        elif i == ')':
            stack.pop()

    if len(stack) == 0:
        return "YES"
    return "NO"

def main():
    T = int(input())
    resultList = list()

    for _ in range(T):
        bracket = str(input())
        resultList.append(validbracket(bracket))

    for i in resultList:
        print(i)

main()