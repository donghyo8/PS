def change(variable_name, file_type):
    if file_type: 
        for i in range(len(variable_name)-1):
            if variable_name[i] == '_':
                if variable_name[i+1] != '_':
                    variable_name[i+1] = variable_name[i+1].upper()
                    res = "".join(variable_name)
                    res = str("".join(res.split("_")))
                else:
                    print("Error!")
                    exit()

    else: 
        idx_list = []
        cursor = 0
        for i in range(len(variable_name)-1):
            if variable_name[i].isupper() :
                idx_list.append(i)

        for idx in idx_list:
            variable_name.insert(idx + cursor, "_")
            cursor += 1

        for i in range(len(variable_name)-1):
            if variable_name[i] == '_':
                variable_name[i+1] = variable_name[i+1].lower()
                res = "".join(variable_name)
    return res


variable_name = list(input())

if '_' in variable_name and variable_name[0].islower():
    file_type = True 
elif not '_' in variable_name and variable_name[0].islower():
    file_type = False 
elif variable_name[0].isupper() or variable_name[0] == '_' or variable_name[-1] == '_':
    print("Error!")
    exit()
    
print(change(variable_name, file_type))
