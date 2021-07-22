S = str(input())

stack = []
temp_list, res = [], []
total = 0

for idx, i  in enumerate(S):
    if i == '(' or i == '[':
        stack.append(i)
        flag = False

    elif i == ')' and stack[-1] == '(' and not flag:
        stack.pop()
        temp_list.append(2)
        flag = True
    elif i == ']' and stack[-1] == '[' and not flag:
        stack.pop()
        temp_list.append(3)
        flag = True
    
    elif i == ')' and stack[-1] == '(' and flag:
        stack.pop()
        temp = temp_list.pop()

        temp_list.append(temp*2)
        
        if len(stack) == 1:
            total = sum(temp_list)

            for i in range(len(temp_list)-1):
                temp_list.pop()
            pre_value = temp_list.pop()
            temp_list.append(total * pre_value)
            flag = False

            
    elif i == ']' and stack[-1] == '[' and flag:
        stack.pop()
        temp = temp_list.pop()
        temp_list.append(temp*3)
        
        if len(stack) == 1:
            total = sum(temp_list)

            for i in range(len(temp_list)-1):
                temp_list.pop()
            pre_value = temp_list.pop()
            temp_list.append(total * pre_value)
            flag = False

    print(temp_list)
if not stack:
    print(sum(temp_list))
else:
    print(0)
