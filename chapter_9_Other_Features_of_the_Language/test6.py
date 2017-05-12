import sys
import getopt

cmdline_params = sys.argv[1:]
opts, args = getopt.getopt(cmdline_params, 'hc:', ['help', 'config='])

for option, parameter in opts:
    if option == '-h' or option == '--help':
        print("this will be printed")
    if option in ('-c', '--config'):
        print("configuration file")

