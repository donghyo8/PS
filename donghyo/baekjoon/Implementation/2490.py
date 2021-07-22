res = []
for _ in range(3):
    arr = list(map(int, input().split()))
    zero_count = arr.count(0)
   
    if zero_count == 0:
        res.append('E')
    elif zero_count == 1:
        res.append('A')
    elif zero_count == 2:
       res.append('B')
    elif zero_count == 3:
       res.append('C')
    else:
       res.append('D')

for i in res:
    print(i)