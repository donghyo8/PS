if __name__ == "__main__":
    variable_type, *variable_info = input().split()

    check = ['[', ']', '&', '*']
    res = []
    for i in variable_info:
        temp = i[:len(i)-1]
        temp = temp[::-1]
        length = len(temp) - 1
        state = True
        re = ''
        idx = 0

        for i, j in enumerate(temp):
            if j == ']':
                re += '['
            elif j == '[':
                re += ']'
            else:
                if j.isalpha():
                    if temp[i-1] in check or state and temp[0].isalpha():
                        re += ' '
                        state = False
                    re += temp[length - idx]
                    idx += 1
                else:
                    re += j
        print(variable_type + re + ';')