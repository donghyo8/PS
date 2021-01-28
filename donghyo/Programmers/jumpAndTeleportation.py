def solution(n):
    ans = 0
    print(bin(n))   

    while n:
        if n % 2 == 1:
            ans += 1
        n = n // 2
    
    print(ans)
    return ans

N1 = 5
N2 = 6
N3 = 5000
solution(N1)