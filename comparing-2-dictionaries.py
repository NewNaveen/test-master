from deepdiff import DeepDiff

a =[{
          "section_id" : "d38cac86-9977-4b5a-87d7-260d093e216e",
          "resource_type" : "FirewallRule",
          "id" : "1024",
          "display_name" : "Default LR Layer3 Rule",
          "sources_excluded" : False,
          "destinations_excluded" : False,
          "action" : "ALLOW",
          "disabled" : False,
          "logged" : False,
          "direction" : "IN_OUT",
          "ip_protocol" : "IPV4_IPV6",
          "is_default" : True,
          "_revision" : 117195
        }]

new = {}
for i in a:
    if ("services" not in i.keys()) and ("sources" not in i.keys()) and ("destinations" not in i.keys()):
        data = {i["id"]: {"services": "all",
                          "sources": "all",
                          "destinations": "all"
               }}
        new.update(data)
print(new)


b = [{
      "section_id" : "6f5e0a70-b8f1-4887-a392-20ad23a9f5bc",
      "resource_type" : "FirewallRule",
      "id" : "8224",
      "display_name" : "default_rule",
      "description" : "default.Policy_Default_Infra-tier0-vmc.default_rule",
      "sources_excluded" : False,
      "destinations_excluded" : False,
      "action" : "DROP",
      "disabled" : False,
      "logged" : False,
      "direction" : "IN_OUT",
      "ip_protocol" : "IPV4_IPV6",
      "is_default" : False,
      "_revision" : 1
    }]

new1 = {}
for j in b:
    if ("services" not in j.keys()) and ("sources" not in j.keys()) and ("destinations" not in j.keys()):
        data = {j["id"]: {"services": "all",
                          "sources": "all",
                          "destinations": "all"
               }}
        new1.update(data)

final = DeepDiff(new, new1)
print(final)

