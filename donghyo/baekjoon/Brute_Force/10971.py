from itertools import permutations
import sys

def solv(number):
    a = 0
    for i in range(N-1):
        if cost_matrix[number[i]][number[i+1]] != 0:
            a += cost_matrix[number[i]][number[i+1]]
        else:
            return -1
        
    if cost_matrix[number[-1]][number[0]] == 0:
        return -1
    else:
        a += cost_matrix[number[-1]][number[0]]
    return a

if __name__ == "__main__":
    N = int(input())
    cost_matrix = [list(map(int, input().split())) for _ in range(N)]
    number = [i for i in range(N)]
    temp = sys.maxsize
    
    for i in permutations(number):
        res = solv(i)

        if res != -1:
            temp = min(temp, res)
    print(temp)
        