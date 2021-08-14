def bracket_check(sentence):
    stack = []

    for i in sentence:
        if i == '(' or i == '[':
                stack.append(i)

        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
    return stack

sentence, res = [], []
while True:
    sentence = list(map(str, input()))

    if sentence[0] == '.':
            break

    bracket_state = bracket_check(sentence)

    if not bracket_state:
        bracket_state = 'yes'
    else:
        bracket_state = 'no'

    res.append(bracket_state)

for i in res:
    print(i)
