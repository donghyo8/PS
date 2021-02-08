def solution(name):
    answer = 0
    tokenList = []
    resultList = []

    if name.isupper() and len(name) >= 1 and len(name) <= 20:
        for i in range(len(name)):
            tokenList.append('A')

            rightAlpha = ord(name[i]) - ord('A')
            leftAlpha = ord('[') - ord(name[i])
            alphaRange = ord(name[i]) - ord(tokenList[i])

            if tokenList[i] != name[i]:
                # A랑 더 가까울때
                if rightAlpha < leftAlpha:
                    resultList.append(chr(ord(tokenList[i]) + alphaRange))

                # A와 Z 거리가 같을때
                elif rightAlpha == leftAlpha:
                    resultList.append(chr(ord(tokenList[i]) + alphaRange))

                # Z랑 더 가까울때
                else:
                    alphaRange = leftAlpha
                    resultList.append(chr(ord('[') - alphaRange))

                answer += alphaRange

            else:
                if name[0] == 'A':
                    resultList.append(name[i])

                elif ord(tokenList[i-2]) < ord(name[i-2]):
                    if rightAlpha < leftAlpha:
                        alphaRange = alphaRange - 1
                        resultList.append(name[i])

                    answer += alphaRange

            answer += 1
            
    print(tokenList)
    print(resultList)
    print(answer -1)
    return answer - 1

solution("AAA")