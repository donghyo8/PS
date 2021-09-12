if __name__ == "__main__":
    S = list(str(input()))

    name_cnt = [0 for _ in range(26)]
    odd = 0
    answer = ''
    temp = ''

    for i in S:
        name_cnt[ord(i)-65] += 1

    for i in range(26):
        if name_cnt[i] % 2 == 1:
            odd += 1
            temp = chr(i+65)
        answer += chr(i+65) * (name_cnt[i] // 2)
    
    rever_answer = list(answer)
    rever_answer.reverse()

    if odd > 1:
        print("I'm Sorry Hansoo")
    else:
        print(answer + temp + "".join(map(str, rever_answer)))
    

    
    