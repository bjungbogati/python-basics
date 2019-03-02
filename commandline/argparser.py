import argparse

# define the program description
text = "This is a help description text. This tells how you can use the argparse module"

# initiate the parser with a description
parser = argparse.ArgumentParser(description = text)  
parser.parse_args() 
