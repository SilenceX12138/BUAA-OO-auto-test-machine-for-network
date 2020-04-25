import os
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path + "./ruler")

from add import add_check
from compare import compare_check
from query import query_check


# valid strip CRLF information list
def get_list(filename):
    result_list = []
    with open(filename, 'r') as f:
        tmp_list = f.readlines()
        for tmp in tmp_list:
            tmp = tmp.strip('\n')
            if (len(tmp) <= 1 or tmp.find("time") != -1):
                continue
            result_list.append(tmp)
    return result_list


# check time limit
def time_judge(output_file):
    with open(output_file, 'r') as f_out:
        last_move = f_out.readlines()[0]
        pos = last_move.index(':')
        time = (float)(last_move[pos + 2:])
        if (time >= 2 - 0.000001):
            return True
    return False


def cmp_judge(data_file, output_file, template_file):
    input_list = get_list(data_file)
    output_list = get_list(output_file)
    template_list = get_list(template_file)

    # filter length difference
    if (len(input_list) != len(output_list)
            or len(input_list) != len(template_list)):
        return "request length has problem"

    # check time
    if (time_judge(output_file)):
        return "time is longer than expected"

    # check correction
    for i in range(len(template_list)):
        if (output_list[i] != template_list[i]):
            return "line " + str(
                i + 1) + " has problem with request: " + input_list[i]

    return ""


def logic_judge(data_file, output_file):
    input_list = get_list(data_file)
    output_list = get_list(output_file)

    valid_id_list = []
    valid_input_list = []

    # filter length difference
    if (len(input_list) != len(output_list)):
        return "request length has problem"

    for i in range(len(input_list)):
        try:
            ins_act = input_list[i].split(' ')[0]
            if (ins_act.find("add") != -1):
                if (add_check(valid_id_list, valid_input_list, input_list[i],
                              output_list[i])):
                    return "line " + str(
                        i + 1) + " has problem with request: " + input_list[i]
                if (ins_act == "add_person"):
                    id = int(input_list[i].split(' ')[1])
                    valid_id_list.append(id)
                elif (ins_act == "add_relation"):
                    id1 = int(input_list[i].split(' ')[1])
                    id2 = int(input_list[i].split(' ')[2])
                    if ((id1 == id2) or (id1 not in valid_id_list)
                            or (id2 not in valid_id_list)):
                        continue
                valid_input_list.append(input_list[i])
            elif (ins_act.find("compare") != -1):
                if (compare_check(valid_id_list, valid_input_list,
                                  input_list[i], output_list[i])):
                    return "line " + str(
                        i + 1) + " has problem with request: " + input_list[i]
            elif (ins_act.find("query") != -1):
                if (i == 42):
                    i = 42
                if (query_check(valid_id_list, valid_input_list, input_list[i],
                                output_list[i])):
                    return "line " + str(
                        i + 1) + " has problem with request: " + input_list[i]

        except (TypeError, ValueError, Exception):
            return "line " + str(
                i + 1) + " has problem with request: " + input_list[i]

    return ""


def check(data_file, output_file, template_file):
    r1 = cmp_judge(data_file, output_file, template_file)
    r2 = logic_judge(data_file, output_file)
    if (len(r1) + len(r2)) > 0:
        return "cmp_judge: " + r1 + "\nlogic_judge: " + r2
    return ""


if __name__ == "__main__":
    r = check("./data/testcase0.txt", "./output/silence/output0.txt",
              "./template/template0.txt")
    print(r)
