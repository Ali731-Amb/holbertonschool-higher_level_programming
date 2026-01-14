#!/usr/bin/python3
for code in range(97, 123):
    if code != 101 and code != 113:  # 101 est 'e', 113 est 'q'
        print("{:c}".format(code), end="")
