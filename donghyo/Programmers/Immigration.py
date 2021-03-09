def solution(n, times):
    answer = 0
    left = 0
    candidate = n
    right = n * max(times) 

    # 최대 시간을 기준으로 검사 가능하면 시간 감소
    while left <= right:
        mid = (left + right) // 2
        succ = 0

        for i in times:
            succ += mid // i
        
        if succ >= candidate:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)

    return answer

solution(6, [7,10])
