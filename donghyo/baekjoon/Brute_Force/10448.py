N = int(input())
temp = [0] * 1001
triangle = [i*(i+1)//2 for i in range(1, 45)]
res = []

for _ in range(N):
    K = int(input())
    
    for i in triangle:
        for j in triangle:
            for k in triangle:
                if i+j+k <= 1000:
                    temp[i+j+k] = 1

    res.append(temp[K])

for i in res:
    print(i)
    