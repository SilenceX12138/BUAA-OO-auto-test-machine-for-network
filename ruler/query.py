import os
import sys
from queue import Queue
import numpy as npy

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path + "./ruler")

from ins_parser import *


def query_val_check(valid_id_list=[],
                    valid_input_list=[],
                    query_input="",
                    output=""):
    id1, id2 = get_two_id_from_ins(query_input)
    if ((id1 not in valid_id_list) or (id2 not in valid_id_list)):
        return not (output == "pinf")
    if (id1 == id2):
        val = int(output)
        return not (val == 0)
    tag = 0
    for valid_input in valid_input_list:
        if (valid_input.find("add_relation") != -1):
            tmp_id_list = [int(info) for info in valid_input.split(' ')[1:3]]
            if ((id1 in tmp_id_list) and (id2 in tmp_id_list)):
                tag = 1
                break
    if (tag == 0):
        return not (output == "rnf")
    val = int(output)
    expected_val = get_val_from_list(valid_input_list, id1, id2)
    return not (val == expected_val)


def query_conflict_check(valid_id_list=[],
                         valid_input_list=[],
                         query_input="",
                         output=""):
    id1, id2 = get_two_id_from_ins(query_input)
    if ((id1 not in valid_id_list) or (id2 not in valid_id_list)):
        return not (output == "pinf")
    input_conflict = int(output)
    character1 = get_character_from_list(valid_input_list, id1)
    character2 = get_character_from_list(valid_input_list, id2)
    return not (input_conflict == character1 ^ character2)


def query_acquaintance_sum_check(valid_id_list=[],
                                 valid_input_list=[],
                                 query_input="",
                                 output=""):
    id = int(query_input.split(' ')[-1])
    if (id not in valid_id_list):
        return not (output == "pinf")
    input_sum = int(output)
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
        return not (output == "pinf")
    rank = int(output)
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
    input_sum = int(output)
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
        return not (output == "pinf")
    if (id1 == id2):
        return not (output == "1")
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
        return not (output == "1")
    return not (output == "0")


def query_group_sum_check(valid_group_dic={}, output=""):
    input_sum = int(output)
    return not (input_sum == len(valid_group_dic))


def query_group_people_sum_check(valid_group_dic={},
                                 query_input="",
                                 output=""):
    id = int(query_input.split(' ')[-1])
    if (id not in valid_group_dic.keys()):
        return not (output == "ginf")
    input_sum = int(output)
    return not (input_sum == len(valid_group_dic[id]))


def query_group_relation_sum_check(valid_input_list=[],
                                   valid_group_dic={},
                                   query_input="",
                                   output=""):
    group_id = int(query_input.split(' ')[-1])
    if (group_id not in valid_group_dic.keys()):
        return not (output == "ginf")
    group_person_list = valid_group_dic[group_id]
    input_sum = int(output)
    expected_sum = len(group_person_list)
    for valid_input in valid_input_list:
        if (valid_input.find("add_relation") != -1):
            id1 = int(valid_input.split(' ')[1])
            id2 = int(valid_input.split(' ')[2])
            if ((id1 in group_person_list) and (id2 in group_person_list)):
                expected_sum += 2
    return not (expected_sum == input_sum)


def query_group_val_sum_check(valid_input_list=[],
                              valid_group_dic={},
                              query_input="",
                              output=""):
    group_id = int(query_input.split(' ')[-1])
    if (group_id not in valid_group_dic.keys()):
        return not (output == "ginf")
    group_person_list = valid_group_dic[group_id]
    input_sum = int(output)
    expected_sum = 0
    for valid_input in valid_input_list:
        if (valid_input.find("add_relation") != -1):
            id1 = int(valid_input.split(' ')[1])
            id2 = int(valid_input.split(' ')[2])
            val = int(valid_input.split(' ')[-1])
            if ((id1 in group_person_list) and (id2 in group_person_list)):
                expected_sum += 2 * val
    return not (expected_sum == input_sum)


def query_group_conflict_sum_check(valid_input_list=[],
                                   valid_group_dic={},
                                   query_input="",
                                   output=""):
    group_id = int(query_input.split(' ')[-1])
    if (group_id not in valid_group_dic.keys()):
        return not (output == "ginf")
    group_person_list = valid_group_dic[group_id]
    input_sum = int(output)
    if (len(group_person_list) == 0):
        return not (input_sum == 0)
    expected_sum = None
    for id in group_person_list:
        character = get_character_from_list(valid_input_list, id)
        if (expected_sum == None):
            expected_sum = character
        else:
            expected_sum ^= character
    return not (expected_sum == input_sum)


def query_group_age_mean_check(valid_input_list=[],
                               valid_group_dic={},
                               query_input="",
                               output=""):
    group_id = int(query_input.split(' ')[-1])
    if (group_id not in valid_group_dic.keys()):
        return not (output == "ginf")
    group_person_list = valid_group_dic[group_id]
    input_mean = int(output)
    if (len(group_person_list) == 0):
        return not (input_mean == 0)
    age_list = []
    for id in group_person_list:
        age = get_age_from_list(valid_input_list, id)
        age_list.append(age)
    expected_mean = int(npy.mean(age_list))
    return not (expected_mean == input_mean)


def query_group_age_var_check(valid_input_list=[],
                              valid_group_dic={},
                              query_input="",
                              output=""):
    group_id = int(query_input.split(' ')[-1])
    if (group_id not in valid_group_dic.keys()):
        return not (output == "ginf")
    group_person_list = valid_group_dic[group_id]
    input_var = int(output)
    if (len(group_person_list) == 0):
        return not (input_var == 0)
    age_list = []
    for id in group_person_list:
        age = get_age_from_list(valid_input_list, id)
        age_list.append(age)
    expected_var = int(npy.var(age_list))
    return not (abs(expected_var - input_var) <= 1)


def query_age_sum_check(valid_id_list=[],
                        valid_input_list=[],
                        query_input="",
                        output=""):
    l = int(query_input.split(' ')[-2])
    r = int(query_input.split(' ')[-1])

    input_sum = int(output)
    expected_sum = 0
    for id in valid_id_list:
        age = get_age_from_list(valid_input_list, id)
        if (age >= l and age <= r):
            expected_sum += 1

    return not (expected_sum == input_sum)


def query_min_path_check(valid_id_list=[],
                         valid_input_list=[],
                         query_input="",
                         output=""):
    id1, id2 = get_two_id_from_ins(query_input)
    if ((id1 not in valid_id_list) or (id2 not in valid_id_list)):
        return not (output == "pinf")
    if (id1 == id2):
        return not (output == "0")
    # paint matrix
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
    # floyd
    for k in range(n):
        for i in range(n):
            if (matrix[i][k] == None):
                continue
            for j in range(n):
                if (i == j or matrix[k][j] == None):
                    continue
                tmpDis = matrix[i][k] + matrix[k][j]
                if (matrix[i][j] == None):
                    matrix[i][j] = tmpDis
                elif (matrix[i][j] > tmpDis):
                    matrix[i][j] = tmpDis

    id1 = valid_id_list.index(int(query_input.split(' ')[1]))
    id2 = valid_id_list.index(int(query_input.split(' ')[2]))
    if (matrix[id1][id2] == None):
        return not (output == "-1")

    return not (output == str(matrix[id1][id2]))


def query_strong_linked_check(valid_id_list=[],
                              valid_input_list=[],
                              query_input="",
                              output=""):
    return False
    # id1, id2 = get_two_id_from_ins(query_input)
    # if ((id1 not in valid_id_list) or (id2 not in valid_id_list)):
    #     return not (output == "pinf")
    # if (id1 == id2):
    #     return not (output == "true")
    # # paint matrix
    # n = len(valid_id_list)
    # matrix = [[None for i in range(n)] for j in range(n)]
    # for valid_input in valid_input_list:
    #     if (valid_input.find("add_relation") != -1):
    #         info_list = valid_input.split(' ')
    #         id1 = valid_id_list.index(int(info_list[1]))
    #         id2 = valid_id_list.index(int(info_list[2]))
    #         value = int(info_list[3])
    #         matrix[id1][id2] = value
    #         matrix[id2][id1] = value
    # id1, id2 = get_two_id_from_ins(query_input)
    # start, end = None, None
    # for i in range(n):
    #     if (valid_id_list[i] == id1):
    #         start = i
    #         if (end != None):
    #             break
    #     if (valid_id_list[i] == id2):
    #         end = i
    #         if (start != None):
    #             break
    # tag = [0 for i in range(n)]
    # path = []
    # from_pos = [-1 for i in range(n)]
    # q = Queue()
    # q.put(start)
    # tag[start] = 1
    # reachable = False
    # while (q.qsize() != 0):
    #     tmp_start = q.get()
    #     for j in range(n):
    #         if (matrix[tmp_start][j] != None and tag[j] == 0):
    #             from_pos[j] = tmp_start
    #             if (j == end):
    #                 while (True):
    #                     last = from_pos[j]
    #                     if (last == start):
    #                         break
    #                     path.append(last)
    #                     j = last
    #                 reachable = True
    #                 break
    #             q.put(j)
    #             tag[j] = 1
    #     if (reachable):
    #         break

    # if (not reachable):
    #     return not (output == "false")

    # tag = [0 for i in range(n)]
    # for v in path:
    #     if ((v == start) or (v == end)):
    #         continue
    #     tag[v] = 1
    # if (len(path) == 0):
    #     matrix[start][end] = None
    #     matrix[end][start] = None
    # q = Queue()
    # q.put(start)
    # tag[start] = 1
    # reachable = False
    # while (q.qsize() != 0):
    #     tmp_start = q.get()
    #     for j in range(n):
    #         if (matrix[tmp_start][j] != None and tag[j] == 0):
    #             if (j == end):
    #                 reachable = True
    #             q.put(j)
    #             tag[j] = 1
    #     if (reachable):
    #         return not (output == "true")

    # return not (output == "false")


def query_block_sum_check(valid_id_list=[], valid_input_list=[], output=""):
    # paint matrix
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
    # floyd
    for k in range(n):
        for i in range(n):
            if (matrix[i][k] == None):
                continue
            for j in range(n):
                if (i == j or matrix[k][j] == None):
                    continue
                tmpDis = matrix[i][k] + matrix[k][j]
                if (matrix[i][j] == None):
                    matrix[i][j] = tmpDis
                elif (matrix[i][j] > tmpDis):
                    matrix[i][j] = tmpDis

    input_sum = int(output)
    if (n == 0):
        return not (input_sum == 0)
    expected_sum = 0
    for i in range(n):
        tag = 0
        for j in range(i):
            if (matrix[i][j] != None):
                tag = 1
        if (tag == 0):
            expected_sum += 1

    return not (input_sum == expected_sum)


def query_money_check(valid_id_list=[],
                      valid_borrow_list=[],
                      query_input="",
                      output=""):
    id = int(query_input.split(' ')[-1])
    if (id not in valid_id_list):
        return not (output == "pinf")

    input_money = int(output)
    expected_money = 0
    for valid_borrow in valid_borrow_list:
        id1 = int(valid_borrow.split(' ')[-3])
        id2 = int(valid_borrow.split(' ')[-2])
        value = int(valid_borrow.split(' ')[-1])
        if (id1 == id):
            expected_money -= value
        elif (id2 == id):
            expected_money += value

    return not (input_money == expected_money)


def query_check(valid_id_list=[],
                valid_input_list=[],
                valid_group_dic={},
                valid_borrow_list=[],
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
    elif ((query_input.find("conflict") != -1)
          and (query_input.find("group") == -1)):
        if (query_conflict_check(valid_id_list, valid_input_list, query_input,
                                 output)):
            return True
    elif (query_input.find("name") != -1):
        if (query_name_rank_check(valid_id_list, valid_input_list, query_input,
                                  output)):
            return True
    elif ((query_input.find("people_sum") != -1)
          and (query_input.find("group") == -1)):
        if (query_people_sum_check(valid_input_list, query_input, output)):
            return True
    elif ((query_input.find("value") != -1)
          and (query_input.find("group") == -1)):
        if (query_val_check(valid_id_list, valid_input_list, query_input,
                            output)):
            return True
    elif (query_input.find("group_sum") != -1):
        if (query_group_sum_check(valid_group_dic, output)):
            return True
    elif (query_input.find("group_people_sum") != -1):
        if (query_group_people_sum_check(valid_group_dic, query_input,
                                         output)):
            return True
    elif (query_input.find("group_relation_sum") != -1):
        if (query_group_relation_sum_check(valid_input_list, valid_group_dic,
                                           query_input, output)):
            return True
    elif (query_input.find("group_value_sum") != -1):
        if (query_group_val_sum_check(valid_input_list, valid_group_dic,
                                      query_input, output)):
            return True
    elif (query_input.find("group_conflict_sum") != -1):
        if (query_group_conflict_sum_check(valid_input_list, valid_group_dic,
                                           query_input, output)):
            return True
    elif (query_input.find("group_age_mean") != -1):
        if (query_group_age_mean_check(valid_input_list, valid_group_dic,
                                       query_input, output)):
            return True
    elif (query_input.find("group_age_var") != -1):
        if (query_group_age_var_check(valid_input_list, valid_group_dic,
                                      query_input, output)):
            return True
    elif (query_input.find("query_age_sum") != -1):
        if (query_age_sum_check(valid_id_list, valid_input_list, query_input,
                                output)):
            return True
    elif (query_input.find("query_min_path") != -1):
        if (query_min_path_check(valid_id_list, valid_input_list, query_input,
                                 output)):
            return True
    elif (query_input.find("query_strong_linked") != -1):
        if (query_strong_linked_check(valid_id_list, valid_input_list,
                                      query_input, output)):
            return True
    elif (query_input.find("query_block_sum") != -1):
        if (query_block_sum_check(valid_id_list, valid_input_list, output)):
            return True
    elif (query_input.find("query_money") != -1):
        if (query_money_check(valid_id_list, valid_borrow_list, query_input,
                              output)):
            return True
    else:
        return True  # illegal instruction

    return False


if __name__ == "__main__":
    r = query_strong_linked_check([1, 2, 3, 4], [
        "add_relation 1 2 1", "add_relation 2 4 1", "add_relation 1 3 1",
        "add_relation 4 3 1"
    ], "query_strong_linked 1 4", "true")
    print(r)
