import argparse

# initiate the parser
parser = argparse.ArgumentParser()

# add long and short argument
parser.add_argument("--time", "-t", help="shutdown time")

# read arguments from the command line
args = parser.parse_args()

# check if --time or -t
if args.time:  
    print("Your computer will shutdown in %s second." % args.time)
