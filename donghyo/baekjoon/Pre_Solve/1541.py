def main():
    N = input().split("-")
    result = 0

    for i in N[0].split("+"):
        result += int(i)

    for i in N[1:]:
        result -= sum(map(int, i.split("+")))
    
    print(result)
main()