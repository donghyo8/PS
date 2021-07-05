def main():
    N, M = map(int, input().split())
    stranger = set()
    notSeen = set()

    for _ in range(N):
        stranger.add(str(input()))

    for _ in range(M):
        notSeen.add(str(input()))

    result = list(stranger & notSeen)

    print(len(result))
    result.sort()
    
    for i in result:
        print(i)
main()