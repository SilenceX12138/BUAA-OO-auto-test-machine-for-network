def add_person_check(valid_id_list=[],
                     valid_input_list=[],
                     input_add="",
                     output=""):
    id = int(input_add.split(' ')[1])
    if (id in valid_id_list):
        return not (output == "epi")
    valid_id_list.append(id)
    valid_input_list.append(input_add)
    return not (output == "Ok")


def add_relation_check(valid_id_list=[],
                       valid_input_list=[],
                       input_add="",
                       output=""):
    id1 = int(input_add.split(' ')[1])
    id2 = int(input_add.split(' ')[2])
    if ((id1 not in valid_id_list) or (id2 not in valid_id_list)):
        return not (output == "pinf")
    if (id1 != id2):
        for valid_input in valid_input_list:
            if (valid_input.find("add_relation") != -1):
                tmp_id_list = [
                    int(info) for info in valid_input.split(' ')[1:3]
                ]
                if ((id1 in tmp_id_list) and (id2 in tmp_id_list)):
                    return not (output == "er")
        valid_input_list.append(input_add)
    return not (output == "Ok")


def add_group_check(valid_group_dic={}, input_add="", output=""):
    id = int(input_add.split(' ')[-1])
    if (id in valid_group_dic.keys()):
        return not (output == "egi")
    valid_group_dic[id] = []
    return not (output == "Ok")


def add_to_group_check(valid_id_list=[],
                       valid_group_dic={},
                       input_add="",
                       output=""):
    person_id = int(input_add.split(' ')[-2])
    group_id = int(input_add.split(' ')[-1])
    if (group_id not in valid_group_dic.keys()):
        return not (output == "ginf")
    if (person_id not in valid_id_list):
        return not (output == "pinf")
    group_person_list = valid_group_dic[group_id]
    if (person_id in group_person_list):
        return not (output == "epi")
    if (len(group_person_list) > 1111):
        return True
    valid_group_dic[group_id].append(person_id)
    return not (output == "Ok")


def add_check(valid_id_list=[],
              valid_input_list=[],
              valid_group_dic={},
              input_add="",
              output=""):
    if (input_add.split(' ')[0] == "add_person"):
        if (add_person_check(valid_id_list, valid_input_list, input_add,
                             output)):
            return True
    elif (input_add.split(' ')[0] == "add_relation"):
        if (add_relation_check(valid_id_list, valid_input_list, input_add,
                               output)):
            return True
    elif (input_add.split(' ')[0] == "add_group"):
        if (add_group_check(valid_group_dic, input_add, output)):
            return True
    elif (input_add.split(' ')[0] == "add_to_group"):
        if (add_to_group_check(valid_id_list, valid_group_dic, input_add,
                               output)):
            return True
    else:
        return True  # illegal instruction
    
    return False


if __name__ == "__main__":
    r = add_to_group_check([1, 2, 3, 4], {1: [1, 2, 3]}, "add_to_group 4 1",
                           "epi")
    print(r)