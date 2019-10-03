""" Filter example: utterance tags

This script demonstrates a simple streaming method to add
<u></u> tags around speakers' speech.

Usage: python3 utterance.py < path/to/input > path/to/output

"""


import sys
import re

in_utterance = False
p = re.compile(r'^([A-Z]+):\s+(.*?)$')


for line in sys.stdin:
    line = line.rstrip()
    m = p.match(line)
    if m:
        if in_utterance:
            print("</u>")
            in_utterance = False
        print("<u who=\"#{}\">{}".format(m.group(1), m.group(2)))
        in_utterance = True
    else:
        print(line)
if in_utterance:
    print("</u>")
