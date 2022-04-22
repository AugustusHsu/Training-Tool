# -*- encoding: utf-8 -*-
'''
@File    :   absl.py
@Time    :   2022/04/19 19:33:07
@Author  :   AugustusHsu
@Contact :   jimhsu11@gmail.com
'''

# here put the import lib
from absl import app
from absl import flags
from absl_otherfile import test

FLAGS = flags.FLAGS
flags.DEFINE_string('name', 'Jane Random', 'Your name.')
flags.DEFINE_string('name2', None, 'Your name.')
flags.DEFINE_boolean('debug2', True, 'Produces debugging output.')
flags.DEFINE_boolean('debug1', False, 'Produces debugging output.')
flags.DEFINE_float('age', None, 'Your age in years.', lower_bound=0)
flags.DEFINE_integer('age2', None, 'Your age in years.', lower_bound=0)
flags.DEFINE_enum('job', 'running', ['running', 'stopped'], 'Job status.')
flags.DEFINE_list('job3',['running', 'stopped'], 'Job status.')

flags.DEFINE_integer('my_version', 0, 'Version number.')
flags.DEFINE_string('filename', None, 'Input file name.', short_name='f')
flags.register_validator('my_version',
                         lambda value: value % 2 == 0,
                         message='--my_version must be divisible by 2')
flags.mark_flag_as_required('filename')

def main(argv):
    test()

if __name__ == '__main__':
    app.run(main)
