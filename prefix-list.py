import json
import re

with open("prefixlist.txt", 'r') as f:

    data = f.readlines()
    new_data = []
    result = []
    prefixlist = []
    for i in data:
        j = i.rstrip('\n')
        new_data.append(j)
    for string in new_data:
        if "Cross VPC route table id:" in string:
            route_table = string.split()[-3]
            result.append(string)
        elif "pl-" in string:
            # print('---'.join(string.split()))
            prefixlist.append(string.split()[0])
            result.append('---'.join(string.split()))
    print(f"Cross VPC Route table: {route_table} has incorrectly programmed these prefixlists: {prefixlist} in the route table")
    print(result)