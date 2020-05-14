import random

two_id_ins_set = []

one_id_ins_set = [
    "query_group_people_sum", "query_group_relation_sum",
    "query_group_value_sum", "query_group_conflict_sum",
    "query_group_age_mean", "query_group_age_var"
]

no_id_ins_set = ["query_group_sum"]


def get_one_id_ins(group_id_list=[]):
    id = random.choice(group_id_list)
    return random.choice(one_id_ins_set) + " " + str(id)


def get_no_id_ins():
    return random.choice(no_id_ins_set)


def get_group_data(group_id_list=[], count=10):
    group_data = []

    for i in range(count):
        chance = random.randint(1, 10)
        if (chance == 10):
            group_data.append(get_no_id_ins())
        else:
            group_data.append(get_one_id_ins(group_id_list))

    random.shuffle(group_data)
    return group_data


if __name__ == "__main__":
    print(get_group_data([1, 2, 3]))
