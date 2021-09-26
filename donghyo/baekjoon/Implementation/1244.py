def create_swtich_table(switch_state):
    dic = {}
    for key, value in enumerate(switch_state):
        dic[key+1] = value
    return dic


def male(dic, received):
    for idx, _ in dic.items():
        if idx % received == 0:
            if dic[idx] == 0:
                dic[idx] = 1
            else:
                dic[idx] = 0


def female(switch_state, dic, received):
    i = 1
    visited = []
    while True:
        if (received - i) < 0 or (received + i) > len(switch_state)-1:
            break

        interval_idx = []
        if switch_state[received-i] == switch_state[received+i]:
            interval_idx = [received-i, received, received+i]

        if len(interval_idx) % 2 != 0:
            for idx in interval_idx:
                if not idx+1 in visited:
                    visited.append(idx+1)
                    if dic[idx+1] == 0:
                        dic[idx+1] = 1
                    else:
                        dic[idx+1] = 0
        i += 1


if __name__ == "__main__":
    switch_n = int(input())
    switch_state = list(map(int, input().split()))
    student_n = int(input())

    dic = create_swtich_table(switch_state)

    for _ in range(student_n):
        sex, received = map(int, input().split())

        if sex == 1:
            male(dic, received)
        else:
            female(switch_state, dic, received-1)
    j = 0
    for res in dic.items():
        if j == 20:
            print()
        else:
            print(res[1], end=' ')
        j += 1