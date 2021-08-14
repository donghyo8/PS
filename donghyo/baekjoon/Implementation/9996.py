N = int(input())
pattern = input().split("*")
start = pattern[0]
end = pattern[1]

res = []
for _ in range(N):
    file_name = str(input())

    if file_name[:len(start)] == start and file_name[-len(end):] == end and len("".join(pattern)) <= len(file_name):
        res.append("DA")
    else:
        res.append("NE")
    
for i in res:
    print(i)