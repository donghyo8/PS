import re

def solution(s):
    answer = ''
    # numbers = numbers = re.findall(r'-?\d+', s)
    numbers = list(map(int, s.split(' ')))
    minNumber = min(numbers)
    maxNumber = max(numbers)

    answer = str(minNumber) + " " + str(maxNumber)
    print(answer)
    return answer


s1 = "1 2 3 4"
s2 = "-1 -2 -3 -4"
s3 = "-1 -1"
solution(s2)