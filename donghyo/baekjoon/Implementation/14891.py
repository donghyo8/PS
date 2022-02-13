from collections import deque
def score_check():
    pass

def rotate(gears, target_gear):

    # target_gear가 0이면 제일 왼쪽이기에 target_gear를 +1씩 len(mapping_state)까지 확인
    # target_gear가 1이면 1을 기준으로, target_gear+1을 len(mapping_state)까지 반복하며 0까지 확인하고, 다시 1을 기준으로 -1씩 0까지 반복하며 확인
    # target_gear가 2라면 기준을 2로하고, 위와 동일
    # target_gear가 3라면 제일 오른쪽이기에 target_gear를 -1씩 0까지 반복하며 확인
    # 이후, 0번 인덱스를 기준으로 점수 체크

    global flag
    print("target_gear ->", target_gear)
    print("fix_target_gear ->", fix_target_gear)

    if target_gear == 0:
        pass
    elif target_gear == 1:
        pass
    elif target_gear == 2:
        if flag: # gear[fixed_target_gear]와 gear[fixed_target_gear + 1] 양극 비교한 후 돌려야함(문제 잘못이해했음;;ㄷㄷ) 무조건 target_gear를 return해서 돌려버리면 안됨(양극을 비교하고 다르면 반대로 회전하고 아닐 때 continue로 가만히 있어야함)
            target_gear = fix_target_gear + 1
            flag = False
            return target_gear
        else:
            for _ in range(2):
                target_gear = target_gear - 1
            return target_gear
    elif target_gear == 3:
        pass
    
    # print(target_gear)
    return target_gear


def rotation_gears(target_gear, state, gears):
    print(gears)        
    print()
    mapping_state = [0, 0, 0, 0]
    check = 0
    temp = 0
    global fix_target_gear
    fix_target_gear = target_gear
    

    while not all(mapping_state):
        
        # 반시계 방향
        if state == -1:
            if check >= 1:
                target_gear = rotate(gears, target_gear)
            queue = deque(gears[target_gear])
            queue.append(queue.popleft())
            gears[target_gear] = list(queue)
            mapping_state[target_gear] = 1

        # 시계 방향
        elif state == 1:
            if check >= 1:
                target_gear = rotate(gears, target_gear)
            queue = deque(gears[target_gear])    
            queue.insert(0, queue.pop())
            gears[target_gear] = list(queue)
            mapping_state[target_gear] = 1

        print(target_gear, ": ", queue, state)
        print(gears)
        print(mapping_state)
        print()

        check += 1
        temp += 1
        if temp == 4:
            break


def gear_state_check(gear_state):
    if gear_state == -1:
        return False
    elif gear_state == 1:
        return True


def start(gears, rotation_method):
    target_gear, gear_state = rotation_method[0], rotation_method[1]

    # 구현 후 해당 state 로직 없애도 될듯
    if gear_state_check(gear_state):
        rotation_gears(target_gear-1, 1, gears)
    else:
        rotation_gears(target_gear-1, -1, gears)


if __name__ == "__main__":
    gear = [list(map(int, input())) for _ in range(4)]
    rotation_method = [list(map(int, input().split())) for _ in range(int(input()))]
    flag = True
    print()

    for target in rotation_method:
        start(gear, target)
        print()
        break
