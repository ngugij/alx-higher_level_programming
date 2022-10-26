#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""


from sys import stdin


size = 0
stat_code = {"200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0}
i = 0
try:
    for line in stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            x = i
            if tokens[-2] in stat_code:
                stat_code[tokens[-2]] += 1
                i = i + 1
            try:
                size = size + int(tokens[-1])
                if x == i:
                    i = i + 1
            except Exception:
                if x == i:
                    continue
        if i % 10 == 0:
            print("File size: {:d}".format(size))
            for key, value in sorted(stat_code.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(size))
    for key, value in sorted(stat_code.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
except KeyboardInterrupt:
    print("File size: {:d}".format(size))
    for key, value in sorted(stat_code.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
