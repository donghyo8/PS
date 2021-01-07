def solution(number, k):

    stack = [number[0]]

    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1 
            stack.pop()
        stack.append(num)

    if k != 0:
        stack = stack[:-k]
    
    # print (''.join(stack))
    return ''.join(stack)


solution("1231234", 3)


    # combinationsList = []
    # combinationsList = list(map(''.join, combinations(number, len(number) - k)))
    # answer = max(combinationsList)
    # print(answer)