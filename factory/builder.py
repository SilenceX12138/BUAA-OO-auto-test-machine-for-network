import random

two_id_ins_set = ["add_to_group", "del_from_froup"]

one_id_ins_set = [
    "add_group"  # <=10
]

no_id_ins_set = []

value_ins_set = ["add_relation", "borrow_from"]

special_ins_set = [
    "add_person"  # <= 800
]


def get_id_list(limit=0):
    id_list = []
    for i in range(random.randint(max(1, limit // 2), limit)):
        id = random.randint(-3 * limit, 3 * limit)
        while id in id_list:
            id = random.randint(-3 * limit, 3 * limit)
        id_list.append(id)
    random.shuffle(id_list)
    return id_list


def get_add_person_list(person_id_list=[]):
    name_list = ["Amy", "Bob", "Candy", "David"]
    add_person_list = []

    for person_id in person_id_list:
        name = random.choice(name_list)
        character = random.randint(0, 666666)
        age = random.randint(0, 2000)
        add_person = "add_person " + str(person_id) + " " + name + " " + str(
            character) + " " + str(age)
        add_person_list.append(add_person)

        # duplicate add_person with one tenth probability
        dupchance = random.randint(1, 20)
        if (dupchance == 20):
            samechance = random.randint(1, 10)
            if (samechance == 10):
                add_person_list.append(add_person)
            else:
                name = random.choice(name_list)
                character = random.randint(0, 666666)
                age = random.randint(0, 2000)
                add_person = "add_person " + str(
                    person_id) + " " + name + " " + str(character) + " " + str(
                        age)
                add_person_list.append(add_person)

    random.shuffle(add_person_list)
    return add_person_list


def get_borrow_from_list(person_id_list=[], count=0):
    borrow_from_list = []

    for i in range(count):
        id1 = random.choice(person_id_list)
        id2 = random.choice(person_id_list)

        value = random.randint(0, 1000)
        borrow_from = "borrow_from " + str(id1) + " " + str(id2) + " " + str(
            value)
        borrow_from_list.append(borrow_from)

    random.shuffle(borrow_from_list)
    return borrow_from_list


def get_add_relation_list(person_id_list=[]):
    add_relation_list = []

    n = len(person_id_list)
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
                        cnt -= 1
                        value = random.randint(0, 1000)
                        matrix[i][j] = 1
                        matrix[j][i] = 1
                        add_relation_list.append("add_relation " +
                                                 str(person_id_list[i]) + " " +
                                                 str(person_id_list[j]) + " " +
                                                 str(value))

    random.shuffle(add_relation_list)
    return add_relation_list


def get_two_id_ins_list(person_id_list=[], group_id_list=[], count=0):
    two_id_ins_list = []

    for i in range(count):
        person_id = random.choice(person_id_list)
        group_id = random.choice(group_id_list)

        chance = random.randint(1, 10)
        if (chance <= 9):
            act = "add_to_group"
        else:
            act = "del_from_group"

        two_id_ins = act + " " + str(person_id) + " " + str(group_id)
        two_id_ins_list.append(two_id_ins)

        # add some del_from_group
        chance = random.randint(1, 10)
        if (chance <= 3):
            two_id_ins = "del_from_group" + " " + str(person_id) + " " + str(
                group_id)
            two_id_ins_list.append(two_id_ins)

    random.shuffle(two_id_ins_list)
    return two_id_ins_list


def get_one_id_ins_list(group_id_list=[]):
    one_id_ins_list = []

    for group_id in group_id_list:
        one_id_ins = random.choice(one_id_ins_set) + " " + str(group_id)
        one_id_ins_list.append(one_id_ins)

    random.shuffle(one_id_ins_list)
    return one_id_ins_list


# one third to two third at tail will be shuffled
def extend_builder_data(basic_builder_data=[],
                        random_builder_data=[],
                        data_list=[]):
    l = len(data_list)
    crit = random.randint(l // 2, l)

    basic_builder_data.extend(data_list[:crit])
    random_builder_data.extend(data_list[crit:])


def get_builder_data(total_count=1000):
    basic_builder_data = []  # contains basic add_person and add_group
    random_builder_data = []

    person_count = min(random.randint(total_count // 6, total_count // 2), 800)
    group_count = random.randint(1, 10)
    borrow_from_count = random.randint(1, max(1, person_count // 3))
    two_id_ins_count = random.randint(1, max(1, person_count))

    person_id_list = get_id_list(person_count)
    group_id_list = get_id_list(group_count)

    add_person_list = get_add_person_list(person_id_list)
    one_id_ins_list = get_one_id_ins_list(group_id_list)
    add_relation_list = get_add_relation_list(person_id_list)
    borrow_from_list = get_borrow_from_list(person_id_list, borrow_from_count)
    two_id_ins_list = get_two_id_ins_list(person_id_list, group_id_list,
                                          two_id_ins_count)

    extend_builder_data(basic_builder_data, random_builder_data,
                        add_person_list)
    extend_builder_data(basic_builder_data, random_builder_data,
                        one_id_ins_list)
    random_builder_data.extend(add_relation_list)
    random_builder_data.extend(borrow_from_list)
    random_builder_data.extend(two_id_ins_list)

    random.shuffle(random_builder_data)
    return person_id_list, group_id_list, basic_builder_data, random_builder_data


if __name__ == "__main__":
    for i in range(10):
        basic_builder_data, random_builder_data = get_builder_data()
        with open("./data/testcase" + str(i) + ".txt", 'w') as f_out:
            for basic_data in basic_builder_data:
                f_out.write(basic_data + "\n")
            for random_data in random_builder_data:
                f_out.write(random_data + "\n")
