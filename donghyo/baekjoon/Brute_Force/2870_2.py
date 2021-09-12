import re
n = int(input()) 
paper = []
res = ''

for i in range(n):
    for j in list(re.split("\D", str(input()))):
        if j != "": 
            paper.append(int(j))

paper.sort()

for i in paper:
    res += str(i)+"\n"
print(res)