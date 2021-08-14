from collections import deque

N = int(input())
word_list = deque([str(input()) for _ in range(N)])
valid_word = word_list.popleft()
word_list = list(word_list)
res = 0

for i in range(N-1):
    compare_word = valid_word[:]
    check_word = word_list[i]

    compare_word = list(compare_word)
    check_word = list(check_word)

    for _ in range(len(check_word)):
        temp = check_word.pop(0)

        if temp in compare_word:
            compare_word.remove(temp)
        else:
            check_word.append(temp)

# 두글자 이상 차이가 나면 하나의 문자를 더하거나 빼도 비슷한 단어가 아니게됨
    if (len(compare_word) == 0 and  len(compare_word) == 0) or (len(compare_word) == 1 and  len(compare_word) == 0) or (len(compare_word) == 0 and  len(compare_word) == 1) or (len(compare_word) == 1 and  len(compare_word) == 1):
        res += 1

print(res) 