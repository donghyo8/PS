#-*-coding:utf-8-*-

import re

def solution(files):
    answer = []
    list = []
    file_len = len(files)

    if file_len <= 1000 :
        for i in files:

            fileName = i
            HEAD = re.compile("[^0-9]")
            HEAD = "".join(HEAD.findall(fileName[0:3]))
            NUMBER = "".join(re.findall("\d+", fileName[:7]))
            NUMBER_INDEX = fileName.find(NUMBER, 0)
            NUMBER_LENGTH = len(NUMBER)

            TAIL = re.compile("[^-]")
            TAIL = "".join(TAIL.findall(fileName[NUMBER_INDEX + NUMBER_LENGTH:]))

            list.append([HEAD, NUMBER, TAIL])
            print(HEAD)
            print(NUMBER)
            print(TAIL)


    sorted_list = sorted(list, key=lambda x:(x[0].lower(), int(x[1])))

    for i in sorted_list:
        answer.append("".join(i))
    print(answer)
    return answer

files1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files2 = ["foo010bar020.zip"]
files3 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
files4 = ["img100.p2ng", "img2020.png123"]
files5 = ["F-15"]

solution(files4)