import random

two_id_ins_set = [
    "query_value",
    "query_conflict",
    "query_circle",
    "query_min_path",
    "query_strong_linked",  # <= 20
    "compare_age",
    "compare_name"
]

one_id_ins_set = [
    "query_acquaintance_sum",
    "query_name_rank",  # <= 1000
    "query_money"
]

no_id_ins_set = ["query_people_sum", "query_block_sum"]

special_ins_set = ["query_age_sum"]


def get_two_id_ins(person_id_list=[]):
    ins = random.choice(two_id_ins_set)
    id1 = random.choice(person_id_list)
    id2 = random.choice(person_id_list)

    two_id_ins = ins + " " + str(id1) + " " + str(id2)
    return two_id_ins


def get_one_id_ins(person_id_list=[]):
    ins = random.choice(one_id_ins_set)
    id = random.choice(person_id_list)

    one_id_ins = ins + " " + str(id)
    return one_id_ins


def get_no_id_ins():
    return random.choice(no_id_ins_set)


def get_special_ins():
    l = random.randint(0, 2000)
    r = l + random.randint(0, 100)

    special_ins = "query_age_sum " + str(l) + " " + str(r)
    return special_ins


def get_network_data(person_id_list=[], count=10):
    network_data = []

    for i in range(count):
        chance = random.randint(1, 14)
        if (chance <= 7):
            network_data.append(get_two_id_ins(person_id_list))
        elif (chance <= 10):
            network_data.append(get_one_id_ins(person_id_list))
        elif (chance <= 12):
            network_data.append(get_no_id_ins())
        elif (chance == 13):
            network_data.append(get_special_ins())

    random.shuffle(network_data)
    return network_data


if __name__ == "__main__":
    print(get_network_data([1, 2, 3]))
