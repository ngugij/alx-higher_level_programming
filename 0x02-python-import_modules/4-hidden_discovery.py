#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    l = dir()
    for s in range(0, len(l)):
        if l[s][0:2] != "__":
            print("{}".format(l[s]))
