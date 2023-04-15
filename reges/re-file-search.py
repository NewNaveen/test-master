import json
import re

"""
This is to open a file and search using regex
We can search using regex in json file also"""
with open("test.json", 'r') as f:
    data = f.readlines()
    regex = re.compile(r'\bdisplay_name')
    for line in data:
        x = regex.search(line)
        if x is not None:
            print(x.string)