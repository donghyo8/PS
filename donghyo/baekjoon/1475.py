def solution():
    N = input()
    count = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in N:
        index = int(i)
        if index == 9:
            index = 6
        count[index] += 1
    
    count[6] = (count[6] + 1) // 2
    print(count)
    print(max(count))
            
solution()