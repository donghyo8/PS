N = input()

count = 0
length = len(N)

for i in range(length-1):
    count += 9 * (10**i) * (i + 1)

count += (int(N) - 10**(length - 1) + 1) * length

print(count)
