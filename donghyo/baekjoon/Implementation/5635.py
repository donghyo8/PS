if __name__ == "__main__":
    n = int(input())
    
    res = []
    for _ in range(n):
        name, d, m, y = input().split()
        res.append([name, int(d), int(m), int(y)])
    
    res = sorted(res, key = lambda x:(x[3], x[2], x[1]))

    max_name = res[0][0]
    min_name = res[n-1][0]
    print(min_name) 
    print(max_name)  
