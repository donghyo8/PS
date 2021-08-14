def solution(enroll, referral, seller, amount):
    fixed_price = 100
    tree = {'-': 'center'}
    money = {'-': 0}

    for i in range(len(enroll)):
        child = enroll[i]
        tree[child] = referral[i]
        money[child] = 0
    
    for i in range(len(seller)):
        seller_name = seller[i]
        parent = tree[seller_name]
        profit = amount[i] * fixed_price
        money[seller_name] += profit

        while True:
            temp = profit // 10
            money[seller_name] -= temp
            money[parent] += temp

            seller_name = parent
            parent = tree[seller_name]
            profit = temp
        
            if parent == 'center':
                break
    
    answer = []
    for i in enroll:
        answer.append(money[i])
    
    return answer

enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"] # 모든 판매원
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"] # 각 판매원을 조직에 참여시킨 다른 판매원의 이름
seller = ["young", "john", "tod", "emily", "mary"] # 판매원
amount = [12, 4, 2, 5, 10] # 판매 수량
solution(enroll, referral, seller, amount)