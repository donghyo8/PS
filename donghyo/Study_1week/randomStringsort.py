#-*-coding:utf-8-*-

def solution(strings, n):
    answer = []

    # key값에 lambda 함수를 이용하여 n번째 인덱스 기준으로 정렬
    answer = sorted(sorted(strings), key=lambda x:x[n])


    print(answer)
    return answer


sortList1 = ["sun", "bed", "car"]
sortList2 = ["abce", "abcd", "cdx"]
n = 1
solution(sortList1, n)