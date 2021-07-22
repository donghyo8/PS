for i in range(int(input())):
    number = int(input())
    convert = bin(number)[2:]
    
    res = ''
    for idx, j in enumerate(convert[::-1]):
        if j == '1':
            res += str(idx) + ' '
    
    print(res)