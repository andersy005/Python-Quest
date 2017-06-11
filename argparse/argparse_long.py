from __future__ import print_function
import argparse

parser = argparse.ArgumentParser(description='Example with long option name')

parser.add_argument('--noarg', action="store_true", default=False)
parser.add_argument('--witharg', action="store", dest="witharg")
parser.add_argument('--witharg2', action="store", dest="witharg2", type=int)

print(parser.parse_args(['--noarg', '--witharg', 'val', '--witharg2=3']))