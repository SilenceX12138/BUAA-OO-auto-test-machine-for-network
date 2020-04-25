def add_person_check(valid_id_list=[],
                     valid_input_list=[],
                     input_add="",
                     output=""):
    id = int(input_add.split(' ')[1])
    if (id in valid_id_list):
        return not (output == "there is another Person has the same id.")
    return not (output == "Ok, Person added.")


def add_relation_check(valid_id_list=[],
                       valid_input_list=[],
                       input_add="",
                       output=""):
    id1 = int(input_add.split(' ')[1])
    id2 = int(input_add.split(' ')[2])
    if ((id1 not in valid_id_list) or (id2 not in valid_id_list)):
        return not (output == "Can't find a Person has this id.")
    for valid_input in valid_input_list:
        if (valid_input.find("add_relation") != -1):
            tmp_id_list = [int(info) for info in valid_input.split(' ')[1:3]]
            if ((id1 in tmp_id_list) and (id2 in tmp_id_list)):
                return not (output == "there is a same Relation.")
    return not (output == "Ok, Relation added.")


def add_check(valid_id_list=[], valid_input_list=[], input_add="", output=""):
    if (input_add.split(' ')[0] == "add_person"):
        if (add_person_check(valid_id_list,valid_input_list, input_add, output)):
            return True
    elif (input_add.split(' ')[0] == "add_relation"):
        if (add_relation_check(valid_id_list, valid_input_list, input_add,
                               output)):
            return True
    return False


if __name__ == "__main__":
    r = add_relation_check([1, 2],
                           ["add_relation 1 1 100", "add_relation 1 2 100"],
                           "add_relation 2 1 100")
    print(r)