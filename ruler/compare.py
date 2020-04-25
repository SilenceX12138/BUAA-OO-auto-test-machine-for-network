import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path + "./ruler")

from ins_parser import get_two_id_from_ins


def compare_age_check(valid_id_list=[],
                      valid_input_list=[],
                      compare_input="",
                      output=""):
    id1, id2 = get_two_id_from_ins(compare_input)
    if ((id1 not in valid_id_list) or (id2 not in valid_id_list)):
        return not (output == "Can't find a Person has this id.")
    r = output.split(' ')[5]  # Ok, the Age of id1 xx the Age of id2.
    age1, age2 = None, None
    for valid_input in valid_input_list:
        if (valid_input.find("add_person " + str(id1) + " ") != -1):
            age1 = int(valid_input.split(' ')[-1])
            if (age2 != None):
                break
        if (valid_input.find("add_person " + str(id2) + " ") != -1):
            age2 = int(valid_input.split(' ')[-1])
            if (age1 != None):
                break
    if (age1 == age2):
        expected_r = " = "
    elif (age1 > age2):
        expected_r = " > "
    else:
        expected_r = " < "
    expected_output = "Ok, the Age of " + str(
        id1) + expected_r + "the Age of " + str(id2) + "."
    return not (output == expected_output)


def compare_name_check(valid_id_list=[],
                       valid_input_list=[],
                       compare_input="",
                       output=""):
    id1, id2 = get_two_id_from_ins(compare_input)
    if ((id1 not in valid_id_list) or (id2 not in valid_id_list)):
        return not (output == "Can't find a Person has this id.")
    r = output.split(' ')[5]  # Ok, the Name of id1 xx the Name of id2.
    name1, name2 = None, None
    for valid_input in valid_input_list:
        if (valid_input.find("add_person " + str(id1) + " ") != -1):
            name1 = valid_input.split(' ')[2]
            if (name2 != None):
                break
        if (valid_input.find("add_person " + str(id2) + " ") != -1):
            name2 = valid_input.split(' ')[2]
            if (name1 != None):
                break
    if (name1 == name2):
        expected_r = " = "
    elif (name1 > name2):
        expected_r = " > "
    else:
        expected_r = " < "
    expected_output = "Ok, the Name of " + str(
        id1) + expected_r + "the Name of " + str(id2) + "."
    return not (output == expected_output)


def compare_check(valid_id_list=[],
                  valid_input_list=[],
                  compare_input="",
                  output=""):
    if (compare_input.find("age") != -1):
        if (compare_age_check(valid_id_list, valid_input_list, compare_input,
                              output)):
            return True
    elif (compare_input.find("name") != -1):
        if (compare_name_check(valid_id_list, valid_input_list, compare_input,
                               output)):
            return True
    return False


if __name__ == "__main__":
    r = compare_age_check(["add_person 1 jack 1 120", "add_person 2 m 2 120"],
                          "compare_age 1 2",
                          "Ok, the Age of 1 = the Age of 2.")
    print(r)
