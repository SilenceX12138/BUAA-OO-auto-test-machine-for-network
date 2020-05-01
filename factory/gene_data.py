import os
import random
import shutil
import sys

from xeger import Xeger

from reg_exp import RegExp

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path + "./factory")

from group_data import get_group_data

two_id_ins_set = [
    "query_value",
    "query_conflict",
    "query_circle",
    "compare_age",
    # "compare_name"
]
one_id_ins_set = ["query_name_rank", "query_acquaintance_sum"]
no_id_ins_set = ["query_people_sum"]
add_ins_set = ["add_person", "add_relation"]

name_list = ["Amy", "Bob", "Candy", "David"]


def get_id_list(limit):
    id_list = []
    for i in range(random.randint(1, limit)):
        id = random.randint(-3 * limit, 3 * limit)
        while id in id_list:
            id = random.randint(-3 * limit, 3 * limit)
        id_list.append(id)
    random.shuffle(id_list)
    return id_list


def get_add_data(id_list=[]):
    add_list = []
    add_list.extend(get_add_person_data(id_list))
    add_list.extend(get_add_relation_data(id_list))
    return add_list


def get_add_person_data(id_list=[]):
    add_person_list = []
    for id in id_list:
        name = random.choice(name_list)
        character = str(random.randint(-10101, 10101))
        age = str(random.randint(0, 200))
        add_person_list.append("add_person " + str(id) + " " + name + " " +
                               character + " " + age)
    return add_person_list


def get_add_relation_data(id_list=[]):
    add_relation_list = []
    n = len(id_list)
    if (n == 1):
        return add_relation_list
    cnt = random.randint(1, n - 1)
    prop = cnt / (n**2 - n)
    matrix = [([0] * n) for i in range(n)]
    while (cnt > 0):
        for i in range(n):
            for j in range(n):
                if (i == j):
                    continue
                if (cnt > 0 and matrix[i][j] == 0):
                    chance = random.random()
                    if (chance <= prop):
                        value = random.randint(1, 150)
                        matrix[i][j] = value
                        matrix[j][i] = value
                        cnt -= 1
                        add_relation_list.append("add_relation " +
                                                 str(id_list[i]) + " " +
                                                 str(id_list[j]) + " " +
                                                 str(value))
    return add_relation_list


def get_two_id_data(id_list=[]):
    id1 = random.choice(id_list)
    id2 = random.choice(id_list)
    while (id1 == id2):
        id2 = random.choice(id_list)
    return random.choice(two_id_ins_set) + " " + str(id1) + " " + str(id2)


def get_one_id_data(id_list=[]):
    id = random.choice(id_list)
    return random.choice(one_id_ins_set) + " " + str(id)


def get_no_id_data():
    return random.choice(no_id_ins_set)


def get_data():
    data_list = []
    # total_cnt = random.randint(500, 1000)
    total_cnt = 100000
    # id_list = get_id_list(max(1, total_cnt // 3))
    id_list = get_id_list(max(1,5000))
    data_list.extend(get_add_data(id_list))
    data_list.extend(get_group_data(id_list, total_cnt // 3))
    left = len(id_list) // 5
    right = len(data_list)
    sub_data_list = data_list[left:right]
    random.shuffle(sub_data_list)
    data_list[left:right] = sub_data_list
    if (total_cnt < len(data_list)):
        total_cnt = len(data_list) + total_cnt // 3
    left_cnt = total_cnt - len(data_list)
    for i in range(left_cnt):
        chance = random.randint(1, 10)
        if (chance <= 1):
            data_list.append(get_no_id_data())
        elif (chance <= 5):
            data_list.append(get_one_id_data(id_list))
        elif (chance <= 10 and len(id_list) >= 2):
            data_list.append(get_two_id_data(id_list))
    chance = random.randint(1, 10)
    if (chance <= 4):
        random.shuffle(data_list)
    if (chance <= 10):
        left = len(data_list) // 3
        right = len(data_list)
        sub_data_list = data_list[left:right]
        random.shuffle(sub_data_list)
        data_list[left:right] = sub_data_list
    return data_list


def gene_data(case_count=10):
    if (os.path.exists("./data")):
        shutil.rmtree("./data")
    os.mkdir("./data")
    for i in range(case_count):
        with open("./data/testcase" + str(i) + ".txt", 'w') as f:
            data_list = get_data()
            for data in data_list:
                f.writelines(data + "\n")


if __name__ == "__main__":
    gene_data()
