def string(N, num, count):
    while True:
        if len(num) == 1:
            num = "0" + num
        
        sum = str(int(num[0]) + int(num[1]))
        num = num[-1] + sum[-1]
        count += 1

        if N == num:
            break

    return count

def integer(N, num, count):
    while True:
        first = num // 10
        second = num % 10
        sum = (first + second) % 10
        num = (second * 10) + sum
        count += 1

        if N == num:
            break

    return count


def main():
    N = input()
    a = num1 = str(N)
    b = num2 = int(N)
    
    count, result1, result2 = 0, 0, 0

    result1 = string(a, num1, count)
    result2 = integer(b, num2, count)

    print(result1)
    print(result2)
    
main()