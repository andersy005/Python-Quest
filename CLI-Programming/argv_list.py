"""
The strange name argv stands for “argument values”. 
Whenever Python runs a program, it takes all of the values 
given on the command line and puts them in the list sys.argv 
so that the program can determine what they were. 
If we run this program with no arguments:
"""

"""the only thing in the list is the full path to our script, 
which is always sys.argv[0]. If we run it with a few arguments,

---
$ python argv_list.py first second third
sys.argv is ['argv_list.py', 'first', 'second', 'third']
"""

import sys
print('sys.argv is', sys.argv)