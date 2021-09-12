from collections import Counter

if __name__ == "__main__":
    N, C = map(int, input().split())
    message = list(map(int, input().split()))

    counter = Counter(message)
    message_sort = sorted(counter.items(), key = lambda x:x[1], reverse=True)

    priority = []
    for i in range(len(message_sort)):
        for j in range(len(message)):
            if message_sort[i][0] == message[j]:
                priority.append(message[j])

    print(' '.join(map(str, priority)))