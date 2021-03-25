from itertools import permutations

def user_check(permutation, banned_id):
    for i in range(len(banned_id)):
        if len(permutation[i]) != len(banned_id[i]):
            return False
        
        for j in range(len(banned_id[i])):
            if permutation[i][j] != banned_id[i][j] and banned_id[i][j] != "*":
                    return False
    return True
            
def solution(user_id, banned_id):
    permutation = list(permutations(user_id, len(banned_id)))
    answer = list()
    temp  = list()

    for i in permutation:
        if user_check(i, banned_id):
            temp.append(sorted(list(i)))

    answer = list(set([tuple(set(temp)) for temp in temp]))
    print(answer)
    print(len(answer))

    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
solution(user_id, banned_id)