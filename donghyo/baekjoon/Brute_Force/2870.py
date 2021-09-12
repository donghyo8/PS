if __name__ == "__main__":
    N = int(input())
    temp_arr = []
    temp = ''
    state = False
    for _ in range(N):
        content = str(input())

        for idx, token in enumerate(content):
            if token.isdigit():
                if token == '0':
                    if idx == len(content)-1:
                        temp_arr.append(int(token))
                    elif content[idx+1].isdigit():
                        continue
                else:
                    temp += token
                    state = True

                    if idx == len(content) - 1:
                        temp_arr.append(int(temp))
            else:
                if state and temp:
                    temp_arr.append(int(temp))
                    temp = ''
                    state = False
        temp = ''

    temp_arr.sort()  
    
    for i in temp_arr:
        if i != '':
            print(i)