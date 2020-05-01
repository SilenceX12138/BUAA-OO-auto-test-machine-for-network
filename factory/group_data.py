import random
import os
import shutil

two_id_ins_set = ["add_to_group"]
# add_group's count should be less than 10, so cannot be added into on_id_ins_set.
one_id_ins_set = [
    "query_group_people_sum",
    "query_group_value_sum",
    "query_group_value_sum",
    "query_group_conflict_sum",
    "query_group_age_mean",
    "query_group_age_var",
    "query_group_age_mean",  # duplicate to make it more occur
    "query_group_age_var",
    "query_group_age_mean",  # duplicate to make it more occur
    "query_group_age_var",
]
no_id_ins_set = ["query_group_sum"]


def get_id_list(limit=10):
    id_list = []
    for i in range(random.randint(1, limit)):
        id = random.randint(-3 * limit, 3 * limit)
        while id in id_list:
            id = random.randint(-3 * limit, 3 * limit)
        id_list.append(id)
    random.shuffle(id_list)
    return id_list


def get_add_data(person_id_list=[], group_id_list=[]):
    add_list = []
    add_list.extend(get_add_group_data(group_id_list))
    add_list.extend(get_add_to_group_data(person_id_list, group_id_list))
    return add_list


def get_add_group_data(id_list=[]):
    add_group_list = []
    for i in range(min(10, len(id_list))):
        id = random.choice(id_list)
        add_group_list.append("add_group " + str(id))
    return add_group_list


def get_add_to_group_data(person_id_list=[], group_id_list=[], limit=10):
    add_to_group_list = []
    for i in range(limit):
        person_id = random.choice(person_id_list)
        group_id = random.choice(group_id_list)
        add_to_group_list.append("add_to_group " + str(person_id) + " " +
                                 str(group_id))
    return add_to_group_list


def get_one_id_data(id_list=[]):
    id = random.choice(id_list)
    return random.choice(one_id_ins_set) + " " + str(id)


def get_no_id_data():
    return random.choice(no_id_ins_set)


def get_group_data(person_id_list=[], limit=10):
    data_list = []
    total_cnt = limit
    group_id_list = get_id_list(min(10, total_cnt // 3))
    data_list = get_add_data(person_id_list, group_id_list)
    if (total_cnt < len(data_list)):
        total_cnt = len(data_list) + total_cnt // 3
    left_cnt = total_cnt - len(data_list)
    for i in range(left_cnt):
        chance = random.randint(1, 5)
        if (chance <= 1):
            data_list.append(get_no_id_data())
        elif (chance <= 5):
            data_list.append(get_one_id_data(group_id_list))
    chance = random.randint(1, 10)
    if (chance > 5):
        random.shuffle(data_list)
    return data_list


def gene_data(case_count=10):
    if (os.path.exists("./data")):
        shutil.rmtree("./data")
    os.mkdir("./data")
    for i in range(case_count):
        with open("./data/testcase" + str(i) + ".txt", 'w') as f:
            data_list = get_group_data([1, 2, 3, 4])
            for data in data_list:
                f.writelines(data + "\n")


if __name__ == "__main__":
    gene_data()