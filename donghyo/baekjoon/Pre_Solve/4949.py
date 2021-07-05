from collections import deque
def main():
    while True:
        stack = deque()
        st = str(input())
        flag = True

        for i in st:
            if i == '(' or i == '[':
                stack.append(i) 

                
            elif i == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    flag = False
                    break
            elif i == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    flag = False
                    break

        if st == '.':
            break    

        if flag:
            print("yes")
        else:
            print("no")  

main()