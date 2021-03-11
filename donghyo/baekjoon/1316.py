def main():

    N = int(input())
    for _ in range(N):
        word = input()

        for i in range(len(word)-1):
            print(word[i], word[i+1])
            if word[i] != word[i+1]:
                if word[i] in word[i+1:]:
                    N -= 1
                    break  
    print(N)
main()