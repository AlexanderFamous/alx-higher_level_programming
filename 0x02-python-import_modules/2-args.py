#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 0
    if len(argv[:-1]) == 1:
        print(len(argv[:-1]), "argument:")
    elif len(argv[:-1]) >= 2:
        print(len(argv[:-1]), "arguments:")
    else:
        print(len(argv[:-1]), "arguments.")
    for i, arg in enumerate(argv[1:]):
        i = i + 1
        print("{}: {}".format(i, arg))
