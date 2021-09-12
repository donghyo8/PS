if __name__ == "__main__":
    N = int(input())
    
    op_dic = {"ADD": 0, "ADDC": 1, "SUB": 2, "SUBC": 3, "MOV": 4, "MOVC": 5, "AND": 6, "ANDC": 7, "OR": 8, "ORC": 9, "NOT": 10, "MULT": 12, "MULTC": 13, "LSFTL": 14, "LSFTLC": 15, "LSFTR": 16, "LSFTRC": 17, "ASFTR": 18, "ASFTRC": 19, "RL": 20, "RLC": 21, "RR": 22, "RRC": 23}

    answer = []
    for _ in range(N):
        opcode, *register = input().split()
        res = ''

        res += bin(op_dic[opcode])[2:].zfill(5)+'0'
        res += bin(int(register[0]))[2:].zfill(3)
        res += bin(int(register[1]))[2:].zfill(3)

        if opcode[-1] == 'C':
            answer.append(res + bin(int(register[2]))[2:].zfill(4))
        else:
            answer.append(res + bin(int(register[2]))[2:].zfill(3)+'0')
    
    for i in answer:
        print(i)