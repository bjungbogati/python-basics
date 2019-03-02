import getopt
import sys


# define the input parameters
options = "cud"
long_options = ["create", "update", "delete"]

# try-catch to process options
try:
    opts, args = getopt.getopt(sys.argv[1:], options, long_options)
    
except getopt.GetoptError as err:
    print (str(err))
    sys.exit(2)

# check and run the commands
for opt, arg in opts:
    if opt in ("-c", "--create"):
        print("[created] a file")
    elif opt in ("-u", "--update"):
        print("[updated] a file")
    elif opt in ("-d", "--delete"):
        print("[deleted] a file")
    else:
        sys.exit(2)