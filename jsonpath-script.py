import json
from jsonpath_ng import jsonpath, parse

json_file = open("output.json")

data = json.load(json_file)
jsonpath_expression = parse('$.result.result.output.results')
# node_id = [for match in jsonpath_expression.find(data) ]
node_id = []
for match in jsonpath_expression.find(data):
    details = match.value
    # print(details)
    for i in details:
        node_id.append(i['node_id'])
    print(node_id)