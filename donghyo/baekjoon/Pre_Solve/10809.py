def main():
    alphaList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    S = str(input())

    for i in range(len(alphaList)):
        print(S.find(alphaList[i]), end = " ")
  
main()
