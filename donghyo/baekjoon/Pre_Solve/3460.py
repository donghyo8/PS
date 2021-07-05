T = int(input())

for i in range(T):
    n = bin(int(input()))[2:]
    count = 0
    
    for i in range(len(n)):
        if n[-i-1] == '1':
            print(count, end = ' ')
            count += 1
        else:
            count += 1
