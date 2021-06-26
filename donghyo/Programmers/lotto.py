def solution(lottos, win_nums):
    answer = []
    max_num_list = []
    min_num_list = []
    dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6}

    lottos.sort()

    for number in lottos:
        if number in win_nums or number == 0:
            max_num_list.append(number)
        if number in win_nums:
            min_num_list.append(number)

    if max_num_list:
        answer.append(dic[len(max_num_list)])
    else:
        answer.append(6)

    if min_num_list:
        answer.append(dic[len(min_num_list)])
    else:
        answer.append(6)

    print(answer)
    return answer


lottos = [1, 2, 3, 4, 5, 6]
win_nums = [38, 19, 20, 40, 15, 25]
solution(lottos, win_nums)
