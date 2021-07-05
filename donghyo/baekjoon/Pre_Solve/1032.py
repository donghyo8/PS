def main():
    fileList = []
    answer = ""

    N = int(input())
    fileList = [str(input()) for _ in range(N)]

    for i in zip(*fileList): # unpacking operator
        if len(set(i)) == 1: # 리스트의 같은 인덱스마다 모두 같은 알파벳일 경우 추가
            answer += i[0]
        else:
            answer += '?'
    
    print(answer)

main()