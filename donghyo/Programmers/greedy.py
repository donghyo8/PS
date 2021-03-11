n = 380
cnt = 0
lst = [500,100,50,10, 5, 1] 
tempList = list()


while n != 0:
    for i in lst:
        r = 0
        r += n // i
        tempList.append(r)
        n -= r * i
        
print(sum(tempList))