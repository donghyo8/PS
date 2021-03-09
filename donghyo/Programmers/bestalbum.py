from collections import defaultdict

def solution(genres, plays):
    answer = []
    full = 2
    dic = defaultdict(list)
    sum_dic = defaultdict(int)

    # hash
    for i, (key, value) in enumerate(zip(genres, plays)):
        dic[key].append([i,value])
    
    # total sum
    for i in range(len(genres)):
        sum_dic[genres[i]] += plays[i]

    for key, value in sorted(sum_dic.items(),reverse=True, key=lambda x:x[1]):
        for i, indexValue in enumerate(sorted(dic[key],reverse=True, key =lambda x:x[1])):
            if i == full:
                break
            answer.append(indexValue[0])
    print(answer)
    return answer


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
solution(genres, plays)