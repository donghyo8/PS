from collections import Counter

def main():
    T = int(input())

    for _ in range(T):
        n = int(input())
        strList = []
        sum = 0
        
        for _ in range(n):
            a, b = input().split()
            strList.append(b)
        
        answer = Counter(strList)
        print(answer)
        result = 1

        for i in answer:
            result *= answer[i] + 1

        print(result-1)
main()