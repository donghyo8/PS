from string import ascii_lowercase

def make_jaum(alpha_list, moum):
    for j in moum:
        if j in alpha_list:
            alpha_list.remove(j)
    return alpha_list

def first_step(S, moum):
    for alpha in moum:
        if alpha in S:
            return True
    return False

def second_step(S, moum, jaum):
    for idx, alpha in enumerate(S):
        if alpha in moum:
            if len(S[idx:]) >= 3 and S[idx] in moum and S[idx+1] in moum and S[idx+2] in moum:
                return False
        else: 
            if len(S[idx:]) >= 3 and S[idx] in jaum and S[idx+1] in jaum and S[idx+2] in jaum:
                return False
    return True

def thrid_step(S):
    state = True
    for idx in range(len(S)):
        if len(S[idx:]) >= 2 and S[idx] == S[idx+1]:
            if (S[idx] == 'e' and S[idx+1] == 'e') or S[idx] == 'o' and S[idx+1] == 'e':
                pass
            else:
                return False
    return state
        
if __name__ == "__main__":
    res = []
    while True:
        S = str(input())
        origin = S

        if S == 'end':
            break

        S = list(S)
        moum = ['a', 'e', 'i', 'o', 'u']
        alpha_list = list(ascii_lowercase)
        jaum = make_jaum(alpha_list, moum)
        
        if first_step(S, moum) and second_step(S, moum, jaum) and thrid_step(S):
            res.append([True, origin])
        else:
            res.append([False, origin])
        
    for state, S in res:
        if state:
            print("<"+ S + "> is acceptable.")
        else:
            print("<"+ S + "> is not acceptable.")