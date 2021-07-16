import re

def remove_Dot(new_id):
    start,  end = None, None

    if new_id[0] == '.':
        start = 1
    if new_id[-1] == '.':
        end = -1

    return new_id[start:end]


def solution(new_id):
    new_id  = new_id.lower()
    new_id = re.sub('[^a-z0-9-_.]', "", new_id)
    new_id = re.sub('[..]+', '.', new_id)
    new_id = remove_Dot(new_id)

    if len(new_id) <= 0:
        new_id = 'a'
    
    if len(new_id) >= 16:
        sub_value = len(new_id) - 15
        new_id = new_id[0:-sub_value]
        
    new_id = remove_Dot(new_id)

    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id

solution("abcdefghijklmn.p")
