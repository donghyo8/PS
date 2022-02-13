from collections import deque


def solv(belt, robots):
    res = 0

    while belt.count(0) < K:
        belt.rotate(1)
        robots.rotate(1)
        robots[-1] = 0

        if sum(robots):
            for idx in range(N-2, -1, -1):
                if robots[idx] and not robots[idx+1] and belt[idx+1]:
                    belt[idx+1] -= 1
                    robots[idx+1], robots[idx] = 1, 0
            robots[-1] = 0


        if not robots[0] and belt[0]:
            belt[0] -= 1
            robots[0] = 1

    return res
    
if __name__ == "__main__":
    N, K = map(int, input().split())
    belt = deque(map(int, input().split()))
    robots = deque([0] *  N)

    print(solv(belt, robots))
