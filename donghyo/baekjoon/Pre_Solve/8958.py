def main():
    T = int(input())

    for _ in range(T):
        ox = str(input())

        sum = 0
        total = 0

        for i in ox:
            if i == 'O':
                sum += 1
            else:
                sum = 0
            
            total += sum
        print(total)
        
main()