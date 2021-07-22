from collections import Counter

s = str(input())
c = Counter(s.upper()).most_common()

max_value = c[0][1]
answer = c[0][0]

for i in range(1, len(c)):
    if max_value < c[i][1]:
        max_value = c[i][1]
        answer = c[i][0]
    elif c[i][1] == max_value:
            print('?')
            exit()
        
print(answer)




