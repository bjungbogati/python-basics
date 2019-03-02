import getopt, sys

argumentList = sys.argv[1:]



unixOpt = "ho:v"  
gnuOpt = ["help", "output=", "verbose"]  

try:  
    arguments, values = getopt.getopt(argumentList, unixOpt, gnuOpt)
    print(arguments)

except getopt.error as err:  
    print (str(err))
    sys.exit(2)


