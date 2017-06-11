from __future__ import print_function
import argparse

parser = argparse.ArgumentParser(description='This an Argparser sample program')

parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print(parser.parse_args(['-a', '-bval', '-c', '3']))



