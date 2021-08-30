N = input()
N = sorted(N, reverse=True)
max_value  = int("".join(N))

if max_value % 30 == 0:
    res = max_value
else:
    res = -1
print(res)