def del_from_group_check(valid_id_list=[],
                         valid_input_list=[],
                         valid_group_dic={},
                         del_input="",
                         output=""):
    person_id = int(del_input.split(' ')[-2])
    group_id = int(del_input.split(' ')[-1])
    
    if (group_id not in valid_group_dic):
        return not (output == "ginf")
    if (person_id not in valid_id_list):
        return not (output == "pinf")
    group_person_list = valid_group_dic[group_id]
    if (person_id not in group_person_list):
        return not (output == "epi")

    group_person_list.remove(person_id)

    return not (output == "Ok")


def del_check(valid_id_list=[],
              valid_input_list=[],
              valid_group_dic={},
              del_input="",
              output=""):

    if (del_from_group_check(valid_id_list, valid_input_list, valid_group_dic,
                             del_input, output)):
        return True

    return False


if __name__ == "__main__":
    r = del_from_group_check([1, 2, 3], [
        "add_person 1 1 1 1", "add_person 2 2 2 2", "add_person 3 3 3 3",
        "add_realtion 1 2 100", " add_relation 2 3 100", "add_to_group 1 2"
    ], {
        1: [0, 1],
        2: [2, 3]
    }, "del_from_group 1 1", "Ok")
    print(r)
