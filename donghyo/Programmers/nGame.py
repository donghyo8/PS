def convert(target_number, convert_number):
    sequence = "0123456789ABCDEF"
    i, j = divmod(target_number, convert_number)

    if i == 0:
        return sequence[j]
    else:
        return convert(i, convert_number) + sequence[j]


def solution(n, t, m, p):
    answer, temp = '', ''
    number = 0

    for i in range(m * t):
        temp += convert(i, n)

    while t > len(answer):
        for i in range(m):
            if p == i + 1:
                answer += temp[number]
            number += 1

    print(answer)
    return answer


solution(16, 16, 2, 1)
