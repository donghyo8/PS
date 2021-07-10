from collections import deque
from itertools import combinations, permutations

while True:
    queue = deque(map(int, input().split()))

    if queue[0] == 0:
        exit()
    
    K = queue[0]
    queue.popleft()

    res = list(combinations(queue, 6))

    for i in res:
        for j in i:
            print(j, end = " ")
        print()
    print()