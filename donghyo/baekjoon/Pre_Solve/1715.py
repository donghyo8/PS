import heapq

def main():
    N = int(input())
    cardList = [int(input()) for _ in range(N)]
    
    heapq.heapify(cardList)
    result = 0

    while True:
        if len(cardList) <= 1:
            break
            
        data1 = heapq.heappop(cardList)
        data2 = heapq.heappop(cardList)

        sum = data1 + data2
        result += sum
        
        heapq.heappush(cardList, sum)

    print(result)
main()