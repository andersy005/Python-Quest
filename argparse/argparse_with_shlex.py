from __future__ import print_function
import argparse
from ConfigParser import ConfigParser
import shlex 

parser = argparse.ArgumentParser(description='Short sample app')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

config = ConfigParser()
config.read('argparse_witH_shlex.ini')
config_value = config.get('options')

print('Config  : {}'.format(config_value))

argument_list = shlex.split(config_value)
print('Arg List: {}'.format(argument_list))

print('Results : {}'.format(parser.parse_args(argument_list)))

