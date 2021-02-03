def solution(s):
    p, y = 0, 0 
    temp = s.lower()
    
    for i in temp:
        if i == 'p':
            p += 1
        elif i == 'y':
            y += 1

    if p != y:
        return False

    return True

solution("pPoooyY")