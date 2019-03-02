from getopt import *
import sys

options = "cud"
long_options = ["create", "update", "delete"]


opts, args = getopt.getopt(sys.argv[1:], options, long_options)

for opt, arg in opts:
    print(opt)
