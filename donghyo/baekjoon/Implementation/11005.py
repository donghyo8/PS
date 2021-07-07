N, B = map(int, input().split())
mapping_str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
res = ''

while N != 0:
    res += mapping_str[N % B]
    N //= B

print(res[::-1])
