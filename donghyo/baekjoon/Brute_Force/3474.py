if __name__ == "__main__":
    T = int(input())

    res = []
    for i in range(T):
        N = int(input())
        zero_cnt = 0
        i = 5 

        while N >= i:
            zero_cnt += N // i
            i *= 5
        res.append(zero_cnt)
    
    for i in res:
        print(i)