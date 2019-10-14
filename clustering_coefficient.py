import numpy as np
import matplotlib.pyplot as plt
import json


if __name__=='__main__':
    path = 'G:\complexnetwork\src1\src1'
    file = []
    file_map = {}
    cc_list = []
    import os
    index = 0
    for i in os.listdir(path):
        file.append(i.split(".")[0])
        file_map[i.split(".")[0]] = index
        index += 1
    index = 0

    cc_record = {}
    with open('cc+.json', "r") as rf:
        cc_list = json.load(rf)['clustering_coefficient']
        for i in cc_list:
            if i in cc_record:
                cc_record[i] += 1
            else:
                cc_record[i] = 1

    for i in file:
        jsname = path + "\\" + i + '.json'
        with open(jsname, "r", errors='ignore', encoding='utf-8') as f:
            jsfile = f.read()
            load_dict = json.loads(jsfile)
            load_dict['cc'] = cc_list[file_map[i]]

        with open('src1\\src1\\' + i + '.json', "w") as wf:
            json.dump(load_dict, wf)