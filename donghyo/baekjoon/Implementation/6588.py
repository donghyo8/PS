from itertools import combinations


def valid(target_number):
    if target_number == 1:
        return False
    else:
        for i in range(2, int(target_number**0.5) + 1):
            if target_number % i == 0:
                return False

        return True


arr = []
sosu = []
limit = 1000001

while True:
    target_number = int(input())

    if 0 == target_number:
        exit()

    if target_number > 4:
        for i in range(1, target_number):
            if valid(i):
                sosu.append(i)

        comb = list(set(combinations(sosu, 2)))
        comb.sort(key=lambda x: int(x[0]))

        for i in comb:
            if (i[0] + i[1]) == target_number:
                arr.append([i[0], i[1]])
                break
        if arr:
            print(str(target_number) + " = " +
                  str(arr[0][0]) + " + " + str(arr[0][1]))
            arr.pop(0)
        else:
            print("Goldbach's conjecture is wrong.")

    else:
        print("Goldbach's conjecture is wrong.")
