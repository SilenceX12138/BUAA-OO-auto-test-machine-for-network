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


def judge(data_file, output_file, template_file):
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


def check(data_file, output_file, template_file):
    return judge(data_file, output_file, template_file)


if __name__ == "__main__":
    r = check("./data/testcase0.txt", "./output/altergo/output0.txt",
              "./template/template0.txt")
    print(r)
