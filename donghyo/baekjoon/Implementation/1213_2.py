import sys

answer = ''
temp = ''
name = str(input())
name_count = [0 for _ in range(26)]

odd = 0
for i in name:
    name_count[ord(i)-65] += 1

for i in range(26):
    if name_count[i] % 2 == 1:
        odd += 1
        temp = chr(i+65)
    answer += chr(i+65) * (name_count[i] // 2)

reverse_answer = list(answer)
reverse_answer.reverse()

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(answer + temp + ''.join(map(str, reverse_answer))) 