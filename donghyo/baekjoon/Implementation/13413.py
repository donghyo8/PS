def goal_check(new_arr):
    if new_arr.count('W') > new_arr.count('B'):
        count = new_arr.count('W')
    else:
        count = new_arr.count('B')
    return count


def create_new_arr(init_state, goal_state):
    new_arr = []
    for idx, token in enumerate(init_state):
        if token != goal_state[idx]:
            new_arr.append(token)
    return new_arr


def run():
    for _ in range(int(input())):
        N = int(input())
        init_state = list(str(input()))
        goal_state = list(str(input()))
        new_arr = create_new_arr(init_state, goal_state)
        count_list.append(goal_check(new_arr))

    return count_list

if __name__ == "__main__":
    count_list = []
    count_list = run()

    for res in count_list:
        print(res)
