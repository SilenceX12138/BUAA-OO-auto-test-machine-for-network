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
            if (len(tmp) == 0 or tmp.find("time") != -1):
                continue
            result_list.append(tmp)
    return result_list


# check time limit
def time_judge(output_file):
    with open(output_file, 'r') as f_out:
        last_move = f_out.readlines()[0]
        pos = last_move.index(':')
        time = (float)(last_move[pos + 2:])
        if (time >= 6.66 - 0.000001):
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
    valid_group_dic = {}

    # filter length difference
    if (len(input_list) != len(output_list)):
        return "request length has problem"

    for i in range(len(input_list)):
        if (i == 617):
            i = 617
        try:
            ins_act = input_list[i].split(' ')[0]
            if (ins_act.find("add") != -1):
                valid_tag = 1
                if (add_check(valid_id_list, valid_input_list, valid_group_dic,
                              input_list[i], output_list[i])):
                    return "line " + str(
                        i + 1) + " has problem with request: " + input_list[i]
            elif (ins_act.find("compare") != -1):
                if (compare_check(valid_id_list, valid_input_list,
                                  input_list[i], output_list[i])):
                    return "line " + str(
                        i + 1) + " has problem with request: " + input_list[i]
            elif (ins_act.find("query") != -1):
                if (i == 0):
                    i = 0
                if (query_check(valid_id_list, valid_input_list,
                                valid_group_dic, input_list[i],
                                output_list[i])):
                    return "line " + str(
                        i + 1) + " has problem with request: " + input_list[i]

        except (TypeError, ValueError, Exception):
            return "line " + str(
                i + 1) + " has problem with request: " + input_list[i]

    return ""


def check(data_file, output_file, template_file):
    # r1 = ""
    r1 = cmp_judge(data_file, output_file, template_file)
    r2 = ""
    # r2 = logic_judge(data_file, output_file)
    if (len(r1) + len(r2)) > 0:
        return "cmp_judge: " + r1 + "\nlogic_judge: " + r2
    return ""


if __name__ == "__main__":
    # for i in range(6):
    #     r = check("./data/testcase" + str(i) + ".txt",
    #               "./output/altergo/output" + str(i) + ".txt",
    #               "./template/template4.txt")
    #     print(i, r)
    r = check("./data/testcase21.txt", "./output/saber/output21.txt",
              "./template/template21.txt")
    print(r)