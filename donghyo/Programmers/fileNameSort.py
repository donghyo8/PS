import re

def solution(files):
    answer = []
    split_list = []

    for fileName in files:
        split_list.append(re.split(r"([0-9]+)", fileName))

    sorted_list = sorted(split_list, key=lambda x:(x[0].lower(), int(x[1])))

    for result in sorted_list:
        answer.append("".join(result))

    print(answer)
    return answer

files1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
files2 = ["foo010bar020.zip"]
files3 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
files4 = ["img100.p2ng", "img2020.png123"]
files5 = ["F-15"]

solution(files3)


# import re

# def solution(files):
#     answer = []
#     split_list = []

#     for fileName in files:
#         head = "".join(re.sub('[^a-zA-Z-]',' ',fileName[0:3]).strip())
#         number = "".join(re.findall("\d+", fileName[:7]))
#         number_index = fileName.find(number, 0)
#         tail = "".join(re.split("([-+]?\b\d+\.\d+\b+)", fileName[number_index + len(number):]))
#         split_list.append([head, number, tail])
        

#     sorted_list = sorted(split_list, key=lambda x:(x[0].lower(), int(x[1])))

#     print(sorted_list)

#     for result in sorted_list:
#         answer.append("".join(result))

#     print(answer)
#     return answer

# files1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
# files2 = ["foo010bar020.zip"]
# files3 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]
# files4 = ["img100.p2ng", "img2020.png123"]
# files5 = ["F-15"]

# solution(files3)
