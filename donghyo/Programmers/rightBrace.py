leftBrace = "("
rightBrace = ")"


def solution(s):
    stack=[]

    for i in s:
        if len(stack) == 0:
            if i=='(':
                stack.append(i)
            else: # 문자열의 첫글자가 ')' 일경우는 애초에 false 이므로 return false
                return False
 
        elif i == '(':
            stack.append(i)
        elif i == ')':
            stack.pop()

    if len(stack) == 0:
        return True
    return False

s1 = "()()"
s2 = "(())()"
s3 = ")()("
s4 = "(()("
s5 = "()))((()"
s6 = "())())"
s7 = "(()))("

solution(s7)