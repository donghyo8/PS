def main():
    N = int(input())
    times = list(map(int,input().split()))
    wait, min = 0, 0


    times.sort()

    for i in range(N):
        min += wait + times[i]
        wait += times[i]
    
    print(min)
        

main()