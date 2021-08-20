def longest_common_subString(s_1, s_2):
    arr_2d = [[0] * (len(s_2)+1) for _ in range(len(s_1) + 1)]
    ans, pos = 0, 0

    for i in range(1, len(s_1)+1):
        for j in range(1, len(s_2)+1):
            if s_1[i-1] == s_2[j-1]:
                arr_2d[i][j] = arr_2d[i-1][j-1] + 1

                if ans < arr_2d[i][j]:
                    ans = arr_2d[i][j]
                    pos = j - 1
    temp = ''
    if pos >= 0:
        for i in range(ans-1, -1, -1):
            temp += s_2[pos-i]
        str = "".join(temp)

    return str, len(str)


def longest_common_subSequence(s_1, s_2):
    arr_2d = [[0] * (len(s_2)+1) for _ in range(len(s_1) + 1)]

    for i in range(1, len(s_1)+1):
        for j in range(1, len(s_2)+1):
            if s_1[i-1] == s_2[j-1]:
                arr_2d[i][j] = arr_2d[i-1][j-1] + 1
            else:
                arr_2d[i][j] = max([arr_2d[i][j-1], arr_2d[i-1][j]])

    temp = ""
    i, j = len(s_1), len(s_2)

    while i != 0 and j != 0:
        if arr_2d[i-1][j] < arr_2d[i][j] and arr_2d[i][j-1] < arr_2d[i][j]:
            temp += s_1[i-1]
            i -= 1
            j -= 1
        elif arr_2d[i-1][j] < arr_2d[i][j]:
            j -= 1
        elif arr_2d[i][j-1] < arr_2d[i][j]:
            i -= 1
        else:
            i -= 1
            j -= 1

    return temp[::-1]


def solv(s_1, s_2):
    arr_2d = [[0] * (len(s_2)+1) for _ in range(len(s_1) + 1)]

    for i in range(1, len(s_1)+1):
        for j in range(1, len(s_2)+1):
            if s_1[i-1] == s_2[j-1]:
                arr_2d[i][j] = arr_2d[i-1][j-1] + 1
            else:
                arr_2d[i][j] = max(arr_2d[i-1][j], arr_2d[i][j-1])

    return arr_2d[-1][-1]


if __name__ == "__main__":
    s_1 = list(map(str, input()))
    s_2 = list(map(str, input()))

    print(longest_common_subString(s_1, s_2))
    print(longest_common_subSequence(s_1, s_2))
    print(solv(s_1, s_2))
