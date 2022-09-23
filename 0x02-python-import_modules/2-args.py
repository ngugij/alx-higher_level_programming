#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    noa = len(argv)

    print("{} argument{}".format(noa - 1, "s" if noa != 2 else ""), end="")
    print("{}".format("." if noa == 1 else ":"))

    i = 1
    for arg in argv[1:]:
        print("{}: {}".format(i, arg))
        i = i + 1
