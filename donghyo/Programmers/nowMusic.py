def time_check(start_time, end_time):
    temp1, temp2 = start_time.split(":"), end_time.split(":")
    hour = int(temp2[0]) - int(temp1[0])
    minutes = int(temp2[1]) - int(temp1[1])

    if hour >= 1:
        minutes += hour * 60

    return minutes


def melody_check(music_info):
    if 'A#' in music_info:
        music_info = music_info.replace('A#', 'A')
    if 'C#' in music_info:
        music_info = music_info.replace('C#', 'C')
    if 'D#' in music_info:
        music_info = music_info.replace('D#', 'D')
    if 'F#' in music_info:
        music_info = music_info.replace('F#', 'E')
    if 'G#' in music_info:
        music_info = music_info.replace('G#', 'F')

    return music_info


def solution(m, musicinfos):
    answer = "(None)"
    res_list = []

    for i in musicinfos:
        temp = i.split(",")
        start_time, end_time = temp[0], temp[1]
        title, music_info = temp[2], temp[3]

        play_time = time_check(start_time, end_time)
        full_melody = melody_check(music_info)
        m = melody_check(m)

        if len(full_melody) <= play_time:
            full_melody = (full_melody * play_time)[:play_time]

        res_list.append([full_melody, title, play_time])

    for res in res_list:
        if m in res[0]:
            answer = res[1]

    print(answer)
    return answer


solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"])
