#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    l = dir(hidden_4)
    for s in l:
        if s[:2] != "__":
            print("{}".format(s))
