def get_two_id_from_ins(ins=""):
    info_list = ins.split(' ')
    return int(info_list[-2]), int(info_list[-1])


def get_val_from_list(valid_input_list=[], id1=0, id2=0):
    val = None
    for valid_input in valid_input_list:
        if (valid_input.find("add_relation " + str(id1) + " " + str(id2)) != -1
                or valid_input.find("add_relation " + str(id2) + " " +
                                    str(id1)) != -1):
            val = int(valid_input.split(' ')[-1])
            break
    return val


def get_character_from_list(valid_input_list=[], id=0):
    character = None
    for valid_input in valid_input_list:
        if (valid_input.find("add_person " + str(id) + " ") != -1):
            character = int(valid_input.split(' ')[3])
            break
    return character


def get_age_from_list(valid_input_list=[], id=0):
    age = None
    for valid_input in valid_input_list:
        if (valid_input.find("add_person " + str(id) + " ") != -1):
            age = int(valid_input.split(' ')[-1])
            break
    return age
