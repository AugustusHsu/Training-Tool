# -*- encoding: utf-8 -*-
'''
@File    :   utils.py
@Time    :   2022/04/19 19:30:52
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
import re
from collections import OrderedDict
import xmltodict
    
def pretty(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))

def CheckPathFlag(ABSLData, ABSLValue):
    # 確保ABSLValue的名稱包含['Path', 'Folder', 'Directory']
    # ABSLValue的個數只能有1個
    path_idx = []
    other_idx = []
    for idx, data in enumerate(ABSLData):
        if ('Path'.casefold() in data[0].casefold() or \
            'Folder'.casefold() in data[0].casefold() or \
            'Directory'.casefold() in data[0].casefold()) and \
            len(ABSLValue[idx]) == 1:
            path_idx.append(idx)
        else:
            other_idx.append(idx)
    return path_idx, other_idx

def GetABSLFlags(python_exe, train_file):
    import subprocess
    r = subprocess.Popen('{} {} --helpxml'.format(python_exe, train_file), stdout=subprocess.PIPE)
    out = r.stdout.read().decode('utf-8')
    d = xmltodict.parse(out, encoding="utf-8")
    flag_list = d['AllFlags']['flag']
    # for item in flag_list:
    #     pretty(item)
    #     print()
    final_dict = {}
    for item in flag_list:
        if not item['file'][:5] == 'absl.':
            item_dict = OrderedDict()
            item_dict['file'] = item['file']
            if len(item['type'].split(' ')) == 5:
                item_dict['type'] = 'list'
            else:
                item_dict['type'] = item['type']
            item_dict['default'] = item['default']
            item_dict['current'] = item['current']
            if len(item['type'].split(' ')) == 2:
                item_dict['enum_value'] = item['enum_value']
            item_dict['meaning'] = item['meaning']
            final_dict[item['name']] = item_dict
    return final_dict

def ParseDict(ABSL_DICT):
    flags = ABSL_DICT.keys()
    value_list = []
    attr_list = []
    for flag_name in flags:
        attr = ABSL_DICT[flag_name]
        attrs = []
        value_list.append([ABSL_DICT[flag_name]['current']])
        for idx, value_name in enumerate(attr):
            if value_name == 'default' or value_name == 'current':
                continue
            # enum_value have 6 column other 5 column
            if idx == 4 and len(attr) == 5:
                attrs.append('')
            attrs.append(ABSL_DICT[flag_name][value_name])
        attr_list.append(attrs)
    return list(flags), value_list, attr_list

def ParseDict2(ABSL_DICT):
    flag_data = {}
    flags = ABSL_DICT.keys()
    for f_idx, flag_name in enumerate(flags):
        attr = ABSL_DICT[flag_name]
        flag_data[f_idx] = {}
        flag_data[f_idx]['value'] = [attr['current']]
        flag_data[f_idx]['info'] = {}
        flag_data[f_idx]['info']['flag'] = flag_name
        flag_data[f_idx]['info']['file'] = attr['file']
        flag_data[f_idx]['info']['type'] = attr['type']
        flag_data[f_idx]['info']['meaning'] = attr['meaning']
        try:
            flag_data[f_idx]['info']['enum_value'] = attr['enum_value']
        except:
            flag_data[f_idx]['info']['enum_value'] = ''
    # pretty(flag_data)
    return flag_data

def ParseJsonParameter(JsonDict):
    value_list = []
    attr_list = []
    flags = []
    for key in JsonDict.keys():
        value_list.append(JsonDict[key]['value'])
        flags.append(JsonDict[key]['info']['flag'])
        # attrs的順序為table上的順序
        attrs = []
        attrs.append(JsonDict[key]['info']['file'])
        attrs.append(JsonDict[key]['info']['type'])
        attrs.append(JsonDict[key]['info']['enum_value'])
        attrs.append(JsonDict[key]['info']['meaning'])
        attr_list.append(attrs)
    return flags, value_list, attr_list
