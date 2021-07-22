from itertools import permutations

N = int(input())
number = list(map(int, input().split()))
op_count = list(map(int, input().split()))
op_list = ['+', '-', '*', '/']
operation = []

for i in range(len(op_count)):
    for j in range(op_count[i]):
        operation.append(op_list[i])

operation = list(set(permutations(operation, len(operation))))
res = []

for op in operation:
    cal = number[0]

    for i in range(1, N):
        if op[i-1] == '+':
            cal += number[i]
        elif op[i-1] == '-':
            cal -= number[i]
        elif op[i-1] == '*':
            cal *= number[i]
        elif op[i-1] == '/':
            cal = int(cal / number[i])

    res.append(cal)
    
print(max(res))
print(min(res))
