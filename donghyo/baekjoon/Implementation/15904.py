S = str(input())
split_data = S.split()
valid_UCPC = ['U', 'C', 'P', 'C']

idx = 0
for word in valid_UCPC:
    if word in S:
        idx += 1
        S = S[S.index(word) + 1:]
    else:
        print('I hate UCPC')
        break
if idx == 4:
    print('I love UCPC')