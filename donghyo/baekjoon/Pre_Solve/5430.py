from collections import deque

def main():
    numberList = list()
    T = int(input())

    for i in range(T):

        
        queue = deque()
        errorflag = False
        Rcount = 0

        exeFunc = str(input())
        n = int(input())

        numberList =(input()[1:-1].split(','))

        if n == 0:
            errorflag = True

        for i in numberList:
            if i != ',':
                queue.append(i)

        for i in range(len(exeFunc)):
            if exeFunc[i] == 'R':
                Rcount += 1
                # numberList.reverse() -> 0(N)

            if exeFunc[i] == 'D':
                if queue:
                    if Rcount % 2 == 1:
                        queue.pop()
                    else:
                        queue.popleft()

                else:
                    errorflag = True
                    break
                
        if errorflag:
            errorflag = False
            print("error")
            
        else:
            if Rcount % 2 == 1:
                queue.reverse()
                print('[' + ','.join(map(str, queue)) + ']')

            else:
                print('[' + ','.join(map(str, queue)) + ']')
            
main()