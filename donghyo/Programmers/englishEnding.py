def solution(n, words):
    answer = []
    checkList = []
    number = 1
    order = 1

    if n >= 2 and n <= 10 and len(words) >= n and len(words) <= 100:
        for i in range(0, len(words)):
            checkWord = words[0]
            
            print(words)
            print(number, order)

            # 이전에 사용한 words 체크 및 소문자 체크
            if checkWord not in checkList and checkWord.islower():
                # words에 1개가 남아 비교할 대상이 없을 경우 result 리턴
                if len(words) > 1:
                    # words의 마지막 글자와 다음 words의 첫글자가 같을 경우 번호와 차례를 계산
                    if checkWord[-1] == words[1][0]: 
                        # 번호와 사람수 n이 같을 경우 한턴을 돌았기때문에 number 1로 초기화
                        if number == n:
                            number = 1
                            order += 1
                        else:
                            number += 1
                        
                    else: # words의 마지막 글자와 다음 words의 첫글자가 같지 않을 경우 result 리턴
                        if number == n: 
                            number = 1
                            order += 1
                        else:
                            number += 1
                        answer = [number, order]
                        break
                        
                    words.pop(0)
                    checkList.append(checkWord)
                    
                # 탈락자가 생기지 않았을 경우
                else:
                    answer = [0, 0]
            else:
                answer = [number, order]
    
    print()          
    print(answer)
    return answer


n = 2
words1 = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"] 
words2 = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
words3 = ["hello", "one", "even", "never", "now", "world", "draw"]
words4 = ["a","aba","aba","a"]
words5 = ["aa", "ab", "bd", "cb" ]
solution(n, words3)




