# -*- encoding: utf-8 -*-
'''
@File    :   utils.py
@Time    :   2022/04/19 19:30:52
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
from collections import OrderedDict
import xmltodict
        
def GetABSLFlags(python_exe, train_file):
    import subprocess
    r = subprocess.Popen('{} {} --helpxml'.format(python_exe, train_file), stdout=subprocess.PIPE)
    out = r.stdout.read().decode('utf-8')
    d = xmltodict.parse(out, encoding="utf-8")
    flag_list = d['AllFlags']['flag']
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
    
