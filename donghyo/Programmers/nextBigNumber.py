def solution(n):
    answer = 0
    prevBin = []
    nextBin = []
    nextNumberList = []
    i = 1 
    count = 0

    if n <= 10000000:
        while(n):
            prevBin = bin(n)
            nextBin = bin(n+i)
            i += 1
    
            if prevBin.count("1") == nextBin.count("1"):
                nextNumberList.append(int(nextBin,2))
                count += 1

            if count == 2:
                answer = min(nextNumberList)
                break

        print(nextNumberList)  
        print(answer)  

    return answer

n1 = 78
n2 = 15
solution(n2)