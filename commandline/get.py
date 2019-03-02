import getopt, sys

argumentList = sys.argv[1:]


unixOpt = "hm:u"  
gnuOpt = ["help", "mode=", "update"]  

try:  
    arguments, values = getopt.getopt(argumentList, unixOpt, gnuOpt)

except getopt.error as err:  
    print (str(err))
    sys.exit(2)


for recentArgument, recentValue in arguments:  
    if recentArgument in ("-h", "--help"):
        print ("activating (help) mode")
    elif recentArgument in ("-u", "--update"):
        print ("starting (update) mode")
    elif recentArgument in ("-m", "--mode"):
        print ("activating (%s) mode" % recentValue)
