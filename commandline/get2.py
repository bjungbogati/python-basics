import getopt
import sys

options = "asm"
long_options = ["add", "sub", "mul"]

# process options
try:
    opts, args = getopt.getopt(sys.argv[1:], options, long_options)
    
except getopt.GetoptError as err:
    print (str(err))
    sys.exit(2)

for arg, val in opts:
    if arg in ("-c", "--create"):
        print("[created] a file")
    elif arg in ("-u", "--update"):
        print("[updated] a file")
    elif arg in ("-d", "--delete"):
        print("[deleted] a file")