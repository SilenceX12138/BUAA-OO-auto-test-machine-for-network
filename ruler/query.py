import os
import sys
from queue import Queue

from ins_parser import *

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path + "./ruler")


def query_val_check(valid_id_list=[],
                    valid_input_list=[],
                    query_input="",
                    output=""):
    id1, id2 = get_two_id_from_ins(query_input)
    if ((id1 not in valid_id_list) or (id2 not in valid_id_list)):
        return not (output == "Can't find a Person has this id.")
    tag = 0
    for valid_input in valid_input_list:
        if (valid_input.find("add_relation") != -1):
            tmp_id_list = [int(info) for info in valid_input.split(' ')[1:3]]
            if ((id1 in tmp_id_list) and (id2 in tmp_id_list)):
                tag = 1
    if (tag == 0):
        return not (output == "can't find the Relation.")
    val = int(output.split(' ')[-1][:-1])
    expected_val = get_val_from_list(valid_input_list, id1, id2)
    return not (val == expected_val)


def query_conflict_check(valid_id_list=[],
                         valid_input_list=[],
                         query_input="",
                         output=""):
    id1, id2 = get_two_id_from_ins(query_input)
    if ((id1 not in valid_id_list) or (id2 not in valid_id_list)):
        return not (output == "Can't find a Person has this id.")
    expected = int(output.split(' ')[-1][:-1])
    character1 = get_character_from_list(valid_input_list, id1)
    character2 = get_character_from_list(valid_input_list, id2)
    return not (expected == character1 ^ character2)


def query_acquaintance_sum_check(valid_id_list=[],
                                 valid_input_list=[],
                                 query_input="",
                                 output=""):
    id = int(query_input.split(' ')[-1])
    if (id not in valid_id_list):
        return not (output == "Can't find a Person has this id.")
    input_sum = int(output.split(' ')[-1][:-1])
    expected_sum = 0
    for valid_input in valid_input_list:
        info_list = valid_input.split(' ')
        if (info_list[0] == "add_relation"):
            if (int(info_list[1]) == id or int(info_list[2]) == id):
                expected_sum += 1
    return not (input_sum == expected_sum)


def query_name_rank_check(valid_id_list=[],
                          valid_input_list=[],
                          query_input="",
                          output=""):
    id = int(query_input.split(' ')[-1])
    if (id not in valid_id_list):
        return not (output == "Can't find a Person has this id.")
    rank = int(output.split(' ')[-1][:-1])
    expected_rank = None
    name_list = []
    for valid_input in valid_input_list:
        if (valid_input.find("add_person") != -1):
            name_list.append(valid_input.split(' ')[2])
            if (id == int(valid_input.split(' ')[1])):
                input_name = name_list[-1]
    name_list = sorted(name_list)
    for i in range(len(name_list)):
        if (name_list[i] == input_name):
            expected_rank = i + 1
            break
    return not (expected_rank == rank)


def query_people_sum_check(valid_input_list=[], query_input="", output=""):
    input_sum = int(output.split(' ')[-1][:-1])
    expected_sum = 0
    for valid_input in valid_input_list:
        if (valid_input.find("add_person") != -1):
            expected_sum += 1
    return not (input_sum == expected_sum)


def query_circle_check(valid_id_list=[],
                       valid_input_list=[],
                       query_input="",
                       output=""):
    id1, id2 = get_two_id_from_ins(query_input)
    if ((id1 not in valid_id_list) or (id2 not in valid_id_list)):
        return not (output == "Can't find a Person has this id.")
    n = len(valid_id_list)
    matrix = [[None for i in range(n)] for j in range(n)]
    for valid_input in valid_input_list:
        if (valid_input.find("add_relation") != -1):
            info_list = valid_input.split(' ')
            id1 = valid_id_list.index(int(info_list[1]))
            id2 = valid_id_list.index(int(info_list[2]))
            value = int(info_list[3])
            matrix[id1][id2] = value
            matrix[id2][id1] = value
    id1, id2 = get_two_id_from_ins(query_input)
    start, end = None, None
    for i in range(n):
        if (valid_id_list[i] == id1):
            start = i
            if (end != None):
                break
        if (valid_id_list[i] == id2):
            end = i
            if (start != None):
                break
    tag = [0 for i in range(n)]
    q = Queue()
    q.put(start)
    tag[start] = 1
    reachable = False
    while (q.qsize() != 0):
        tmp_start = q.get()
        for j in range(n):
            if (matrix[tmp_start][j] != None and tag[j] == 0):
                if (j == end):
                    reachable = True
                q.put(j)
                tag[j] = 1
    if (reachable):
        return not (output == "they will in circle")
    return not (output == "they won't in circle")


def query_check(valid_id_list=[],
                valid_input_list=[],
                query_input="",
                output=""):
    if (query_input.find("acquaintance") != -1):
        if (query_acquaintance_sum_check(valid_id_list, valid_input_list,
                                         query_input, output)):
            return True
    elif (query_input.find("circle") != -1):
        if (query_circle_check(valid_id_list, valid_input_list, query_input,
                               output)):
            return True
    elif (query_input.find("conflict") != -1):
        if (query_conflict_check(valid_id_list, valid_input_list, query_input,
                                 output)):
            return True
    elif (query_input.find("name") != -1):
        if (query_name_rank_check(valid_id_list, valid_input_list, query_input,
                                  output)):
            return True
    elif (query_input.find("sum") != -1):
        if (query_people_sum_check(valid_input_list, query_input, output)):
            return True
    elif (query_input.find("value") != -1):
        if (query_val_check(valid_id_list, valid_input_list, query_input,
                            output)):
            return True

    return False


if __name__ == "__main__":
    # r = query_people_sum_check([
    #     "add_person 1 jack 2 120", "add_person 2 jack 20 120",
    #     "add_relation 1 2 100"
    # ], "query_name_rank", "Ok, the rank of 1 is 1.")
    # print(r)
    print(
        query_circle_check([1, 2], [
            "add_relation 1 2 -100", "add_relation 2 4 -100",
            "add_relation 4 3 -100", "add_realtion 3 2 -100"
        ], "queryCircle 1 3", "they will in circle"))
