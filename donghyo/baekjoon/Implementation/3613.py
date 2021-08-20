def print_Error():
    print("Error!")
    exit()

def file_type_check(data):
    if '_' in data:
        sub_idx = 0
        for idx, token in enumerate(data):
            if idx == 0 and not data[idx].islower() or token.isupper():
                    print_Error()
            elif token == '_':
                if token == '_' and idx == 0 or len(data) == idx + 1:
                    print_Error()

                underbar_idx.append(idx)
                underbar_next_idx.append(idx + 1)

                if data[underbar_next_idx[sub_idx]].islower():
                    state = True
                    sub_idx += 1
                else:
                    print_Error()
    else:
        state = False
        for idx, token in enumerate(data):
            if idx == 0 and data[idx].isupper():
                print_Error()
            elif token.isupper() and idx > 0:
                underbar_idx.append(idx)
                underbar_next_idx.append(idx - 1)
            elif token == " " or token == '_':
                print_Error()
    return state

def cpp_by_java_change(data):
    for idx_1, idx_2 in zip(underbar_idx, underbar_next_idx):
        data[idx_1] = ""
        convert_alpha = data[idx_2].upper()
        data[idx_2] = convert_alpha

    return "".join(data)

def java_by_cpp_change(data):
    for idx_1, idx_2 in zip(underbar_idx, underbar_next_idx):
        data[idx_1] = data[idx_1].lower()
        data[idx_2] += '_'

    return "".join(data)

if __name__ == "__main__":
    underbar_idx, underbar_next_idx = [], []
    S = list(str(input()))

    if bool(file_type_check(S)):
        print(cpp_by_java_change(S))
    else:
        print(java_by_cpp_change(S))
