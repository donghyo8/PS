leftBrace = "("
rightBrace = ")"

# 괄호가 올바른 문자열인지 검증하는 함수
# 루프를 돌며 각 괄호마다 개수를 카운트하고 비교
def validBrace(p):
    leftCount = 0
    rightCount = 0
    for i in p:
        if (i == leftBrace):
            leftCount += 1
        else:
            rightCount += 1
        if (leftCount < rightCount):
            return False
    return True

def solution(p):
    answer = ''
    u = []
    v = []
    leftCount = 0
    rightCount = 0

    # 빈 문자열 확인
    if(p == ''):
        return answer

    # 균형잡힌 괄호 문자열  u, v 분할
    for index, i in enumerate(p):
        if(i == leftBrace):
            leftCount += 1
        elif(i == rightBrace):
            rightCount += 1
        if(leftCount == rightCount):
            u = p[:index + 1]
            v = p[index + 1:]
            break

    # 올바른 괄호 체크
    if (validBrace(u) == True):
        # u에 이어붙임
        answer = u + solution(v)
    else:
        # 빈 문자열에 첫번째 문자로 ( 이어붙임
        # 문자열 v에 대해 재귀적으로 문자열 이어붙임
        # 다시 ) 이어붙임
        # 맨앞 맨뒤 문자 제거
        answer += leftBrace + solution(v) + rightBrace
        u = u[1:-1]

        # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 이어붙임
        appendTemp = ''
        for i in u:
            if i == leftBrace:
                appendTemp += rightBrace
            else:
                appendTemp += leftBrace
        answer += appendTemp
    print(answer)
    return answer


p1 = "(()())()"
p2 = ")("
p3 = "()))((()"
p4 = ''
solution(p3)

## 올바른 괄호 -> (, ) 개수와 괄호 짝도 맞을 경우 올바른
## 균형잡힌 -> (, )의 개수가 같으면 균형
