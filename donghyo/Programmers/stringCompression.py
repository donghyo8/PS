#-*-coding:utf-8-*-

def solution(s):
    answer = 0
    strList = s
    length = []
    index = 1

    # s 유효성 검사
    if len(s) == 0 | len(s) > 1000 :
        return 0
    
    ## strList를 증가되는 인덱스값만큼 슬라이싱
    for index in range(index, len(s) + 1): 
        result = ""
        slice = strList[0:index]
        count = 1
        
        # 슬라이싱된 문자열이 루프도는 strList의 문자열과 같으면 카운트 증가 
        for j in range(index, len(s), index):
            if strList[j:j+index] == slice:
                count += 1
            # 같지 않다면 카운트값을 체크하고 카운트 제거
            else:
                if count == 1:
                    count = ""
                # count값을 문자열로 컨버팅하여 슬라이싱된 문자열앞에 이어붙임
                result += str(count) + slice
                slice = strList[j:j+index]
                count = 1
 
        if count == 1:
            count = ""
        
        # 이중 루프를 돌며 압축된 문자열들의 길이를 length 배열에 시퀀셜하게 담음
        # length 리스트 내 최소 값 answer
        result += str(count) + slice
        print(result)
        length.append(len(result))
        result = ""
        answer = min(length)
        print(length[-1:index])
        
    print(answer)
    return answer


s = "a"
solution(s)

