def main():
    s = str(input())
    count = 0
    
    for _ in s.split():
        count += 1

    print(count)
main()