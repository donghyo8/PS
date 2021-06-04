def solution(money, cost):
    answer = -1
    count_list = []
    idx = 1

    while True:
        if idx == len(cost)+1:
            answer = max(count_list)
            return answer

        temp = cost[idx-1]
        count = 0

        for i in range(idx, len(cost)):
            temp += cost[i]

            if temp > money:
                temp -= cost[i]
            else:
                count += 1

        idx += 1
        count_list.append(count)

solution(100, [245, 317, 151, 192])
