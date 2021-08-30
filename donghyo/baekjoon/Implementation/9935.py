def solution():
    normal_Str = list(input())
    explosion_Str = list(input()) 
    len_normoal = len(normal_Str)
    len_explosion = len(explosion_Str)
    stack = []

    for i in normal_Str:
        stack.append(i)
        
        if len(stack) >= len_explosion:
            if stack[-len_explosion:] == explosion_Str:
                for _ in range(len_explosion):
                    stack.pop() 
    return stack

def main():
    result = solution()

    if result:
        print("".join(result))
    else:
        print("FRULA")

main()

