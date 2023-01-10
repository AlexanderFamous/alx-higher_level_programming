#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    if len(sys.argv[:-1]) >= 1:
        print(len(sys.argv[:-1]), "arguments:", end="\n")
        for i, arg in enumerate(sys.argv[1:]):
            i = i + 1
            print("{}:  {}".format(i, arg))
    else:
        print(len(sys.argv[:-1]), "argument.")
