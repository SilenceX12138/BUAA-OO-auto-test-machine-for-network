import os
import random
import shutil
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path + "./factory")

from builder import get_builder_data
from group_data import get_group_data
from network_data import get_network_data
from xeger import Xeger
from reg_exp import RegExp


def get_data(count=3000):
    data = []
    random_data = []

    person_id_list, group_id_list, basic_builder_data, random_builder_data = get_builder_data(
        count)

    l1 = len(basic_builder_data) + len(random_builder_data)
    l2 = (count - l1) // 3
    l3 = count - l1 - l2

    group_data = get_group_data(group_id_list, l2)
    network_data = get_network_data(person_id_list, l3)

    random_data.extend(random_builder_data)
    random_data.extend(group_data)
    random_data.extend(network_data)

    random.shuffle(random_data)
    data = basic_builder_data + random_data

    return data


def gene_data(case_count=100):
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
