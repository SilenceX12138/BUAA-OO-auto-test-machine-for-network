import os
import shutil
import time
from random import random
from subprocess import PIPE, Popen
from sys import argv


def get_output(dirname, datadir):
    if (dirname == "std"):
        class_path = "./ruler/" + dirname
        output_path = "./template"
    else:
        class_path = "./lib/" + dirname
        output_path = "./output/" + dirname

    if (os.path.exists(output_path)):
        shutil.rmtree(output_path)
    os.mkdir(output_path)

    case_count = len(os.listdir(datadir))
    for i in range(case_count):
        data_file = datadir + "/testcase" + str(i) + ".txt"
        if (dirname != "std"):
            output_file = output_path + "/output" + str(i) + ".txt"
        else:
            output_file = output_path + "/template" + str(i) + ".txt"

        if (os.getcwd().find('\\') != -1):
            ''' evaluate real time on win '''
            start_time = time.time()
            os.system("java -jar " + class_path + "/3-1.jar < " + data_file +
                      " > " + output_file)
            end_time = time.time()
            real_time = end_time - start_time
            with open(output_file, 'r') as f_out:
                output_list = f_out.readlines()
            with open(output_file, 'w') as f_out:
                f_out.writelines("real time: " + str(real_time) + "\n")
                f_out.writelines(output_list)
        else:
            ''' evaulate cpu time on linux '''
            r = Popen("time java -jar " + class_path + "/3-1.jar < " +
                      data_file + " > " + output_file,
                      stderr=PIPE,
                      shell=True)
            s = str(r.stderr.read()).replace('\'', '')[1:]
            usr_time = float(s.split(' ')[0][:-4])
            sys_time = float(s.split(' ')[1][:-6])
            cpu_time = sys_time + usr_time
            with open(output_file, 'r') as f_out:
                output_list = f_out.readlines()
            with open(output_file, 'w') as f_out:
                f_out.writelines("cpu time: " + str(cpu_time) + "\n")
                f_out.writelines(output_list)


if __name__ == "__main__":
    # dirname = argv[1]
    # datadir = argv[2]
    # get_output(dirname, datadir)
    get_output("silence", "./data")
