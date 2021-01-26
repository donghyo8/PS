import re
import collections

def solution(s):
    answer = []

    splitNumber = collections.Counter(re.findall('\d+',s))
    result = sorted(splitNumber.items(), key=lambda x: x[1], reverse=True)

    for i in range(len(result)):
        answer.append(int(result[i][0]))

    print(answer)
    return answer

s1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s3 = "{{20,111},{111}}"
s4 = "{{123}}"
s5 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
solution(s5)