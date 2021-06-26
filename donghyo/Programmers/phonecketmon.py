def solution(nums):
    answer = 0

    if len(nums) >= 1 and len(nums) <= 10000 and len(nums) % 2 == 0:
        selectCount = len(nums) / 2
        new_List = list(set(nums))

        for i in new_List:
            if answer < selectCount:
                answer += 1

        # temp = len(new_List) - selectCount
        # if temp > 0:
        #     new_List.pop()

        # answer = len(new_List)

        print(new_List)
        print(answer)

    return answer


nums1 = [3, 1, 2, 3]
nums2 = [3, 3, 3, 2, 2, 4]
nums3 = [3, 3, 3, 2, 2, 2]

solution(nums1)
