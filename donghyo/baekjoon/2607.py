from collections import Counter

N = int(input())
arr = [input() for _ in range(N)]
word = {}

for i in arr[0]:
    if i in word:
        word[i] += 1
    else:
        word[i] = 1

word = sorted(word.items())

idx = 1
res = 0

while True:
    valid_word = {}
    if idx == N:
        break

    for token in arr[idx]:
        if token in valid_word:
            valid_word[token] += 1
        else:
            valid_word[token] = 1

    #
    valid_word = sorted(valid_word.items())
    a = (set(word) - set(valid_word))
    b = (set(valid_word) - set(word))

    for i, j in zip(a, b):
        key1, value1 = i[0], i[1]
        key2, value2 = j[0], j[1]
        print(key1, value1)
        print(key2, value2)
        # new_word = {}
        # new_valid_word = {}

        new_word, new_valid_word = dict(word), dict(valid_word)

        if key1.isupper() and key2.isupper():
            if key1 == key2:
                new_word[key2] += 1
                new_valid_word[key1] -= 1

                if new_word == arr[idx] and new_valid_word == arr[0]:
                    res += 1
        else:
            res += 1
    idx += 1

print(res)
