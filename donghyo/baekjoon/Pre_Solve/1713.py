N = int(input())
total = int(input())
student = list(map(int, input().split()))
frame, count = [], []

for i in student:
    if i in frame:
        idx = frame.index(i)
        count[idx] += 1
    else:
        if N <= len(frame):
            del frame[count.index(min(count))]
            del count[count.index(min(count))]

        frame.append(i)
        count.append(1)
        
frame.sort()
print(' '.join(map(str, frame)))