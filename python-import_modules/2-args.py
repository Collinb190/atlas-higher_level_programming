#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argNum = len(sys.argv) - 1
    if argNum == 0:
        print("{} arguments.".format(argNum))
    elif argNum == 1:
        print("{} argument:\n{}: {}".format(argNum, argNum, sys.argv[1]))
    else:
        print("{} arguments:".format(argNum))
        for i in range(1, argNum + 1):
            print("{}: {}".format(i, sys.argv[i]))
