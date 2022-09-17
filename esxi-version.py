import json

f = open('transport-nodes.json')
data = json.load(f)

for i in data["results"]:
    if "os_type" in i["node_deployment_info"]:
        if i["node_deployment_info"]["os_type"] == "ESXI":
                print(f"{i['node_deployment_info']['display_name']} version is : {i['node_deployment_info']['os_version']}")
