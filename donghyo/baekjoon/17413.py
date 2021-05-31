S = str(input())
state = False
result, temp = '', ''
idx = 0

for i in S:
    if i == '<':
        result += i
        state = True
    elif i == '>':
        result += i
        state = False
    elif state == True:
        result += i

    elif state == False:
        temp += i

        if i == ' ' :
            result += ''.join(reversed(temp.replace(" ", "")))
            result += ' '
            temp = ''
        elif len(S) == idx + 1: 
            result += ''.join(reversed(temp))
        
        elif S[idx+1] == '<':
            result += ''.join(reversed(temp))
            temp = ''

    idx += 1

print(result)




