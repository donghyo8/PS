# name = str(input())

# arr = [0] * len(name)
# arr_count = {}
# state = True
# result = ''
# idx = 0
# arr[0] = name[0]


# for i in name:
#     arr_count[i] = name.count(i)

#     if arr_count[i] % 2 == 0:
#         if name != ''.join(reversed(name)):
#             if arr[idx] in arr_count.keys():
#                 arr[idx-1] = i
#             else:
#                 if arr.count(i) <= len(arr_count):
#                     arr[idx] = i
#                 else:
#                     arr[idx+1] = i

#             print(arr)

#         else:
#             result = name
#     else:
#         state = False

#     idx += 1

# if state:
#     print(result)
# else:
#     print("I'm Sorry Hansoo")