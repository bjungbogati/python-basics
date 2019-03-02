import argparse

# initialize the parser
parser = argparse.ArgumentParser()  
parser.add_argument("-V", "--version", help="show argument parser version", action="store_true")

# read command line argument
args = parser.parse_args()

# check for --version or -V
if args.version:  
    print("Argparser version 0.1")

