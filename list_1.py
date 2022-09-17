import json

new_path = ["policy/api/v1/infra/tier-1s/cgw", "policy/api/v1/infra/tier-1s/mgw", "policy/api/v1/infra/tier-0s/vmc"]

# dict1 = {"vmc": "Policy_Default_Infra", "Management Gateway": "Policy_Default_Infra"}
dict1 = {}
dict2 = {"vmc": "Policy_Default_Infra", "Management Gateway": "Policy_Default_Infra", "Compute Gateway": "Policy_Default_Infra"}

diff_dict = {}

with open("output.json", "r") as f:
    data = f.read()
    new = json.loads(data)
    result = {}
    for i in new["results"]:
        if "applied_tos" in i.keys() and (i.get("tags")[0].get("tag") == "/infra/domains/default/gateway-policies/Policy_Default_Infra-tier0-vmc" or
                                            i.get("tags")[0].get("tag") == "/infra/domains/default/gateway-policies/Policy_Default_Infra-tier1-mgw" or
                                            i.get("tags")[0].get("tag") == "/infra/domains/default/gateway-policies/Policy_Default_Infra-tier1-cgw"):
            result.update({i["applied_tos"][0]["target_display_name"]: i["display_name"]})
    print(result)
