def solution(a, b):
    answer = ''
   
    for i in range(b):
        for j in range(a):
            print('*', end = '')
        print()


    return answer

# a, b = map(int, input().strip().split(' '))
# for i in range(b):
#     for j in range(a):
#         print('*', end = '')
#     print()



solution(5, 3)