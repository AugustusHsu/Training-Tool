# -*- encoding: utf-8 -*-
'''
@File    :   absl_otherfile.py
@Time    :   2022/04/19 19:33:51
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
from absl import flags
FLAGS = flags.FLAGS
flags.DEFINE_string('test_var', 'test_name', 'test_description')
flags.DEFINE_enum('job2', 'running', ['running', 'stopped'], 'Job status.')

def test():
    print(FLAGS.test_var)