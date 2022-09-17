import json
import openpyxl
import pandas as pd


with open("sddc_id.json", 'r') as f:
    data = f.read()
    # Final output
    final_data = []
    # stale rule details
    stale_rule = []
    new_data = json.loads(data)
    for i in new_data["output"]:
        if type(i["result"]["output"]) is dict and type(i["result"]["output"]["stale_rules"]) is list:
            stale_rule.append(i)

    for j in stale_rule:
        x = {"sddc_id": j["sddc_id"],
             "stale_rules": j["result"]["output"]["stale_rules"],
             "zero_hit_session_count": j["result"]["output"]["zero_hit_session_count"],
             "nonzero_hit_session_count": j["result"]["output"]["nonzero_hit_session_count"],
             "anyanyallow": j["result"]["output"]["anyanyallow"]}
        final_data.append(x)
    rule1 = []
    rule1024 = []
    rule25 = []
    rule610 = []
    rule1120 = []
    rule21 = []
    others = []
    for k in final_data:
        if (len(k["stale_rules"]) == 1) and (k["stale_rules"][0] != '1024'):
            rule1.append(k)
        elif (len(k["stale_rules"]) == 1) and (k["stale_rules"][0] == '1024'):
            rule1024.append(k)
        elif (1 < len(k["stale_rules"]) <= 5) and len(k["nonzero_hit_session_count"]) >= 1:
            rule25.append(k)
        elif (5 < len(k["stale_rules"]) <= 10) and len(k["nonzero_hit_session_count"]) >= 1:
            rule610.append(k)
        elif (10 < len(k["stale_rules"]) <= 20) and len(k["nonzero_hit_session_count"]) >= 1:
            rule1120.append(k)
        elif (len(k["stale_rules"]) > 20) and len(k["nonzero_hit_session_count"]) >= 1:
            rule21.append(k)
        else:
            others.append(k)
    df1 = pd.DataFrame.from_dict(rule1024)
    df2 = pd.DataFrame.from_dict(rule1)
    df3 = pd.DataFrame.from_dict(rule25)
    df4 = pd.DataFrame.from_dict(rule610)
    df5 = pd.DataFrame.from_dict(rule1120)
    df6 = pd.DataFrame.from_dict(rule21)
    df7 = pd.DataFrame.from_dict(others)

    with pd.ExcelWriter("output1.xlsx") as writer:
        df1.to_excel(writer, index=False, sheet_name='rule-1024', engine='xlsxwriter')
        df2.to_excel(writer, index=False, sheet_name='single-rules')
        df3.to_excel(writer, index=False, sheet_name='rule-count-2-to-5')
        df4.to_excel(writer, index=False, sheet_name='rule-count-6-to-10')
        df5.to_excel(writer, index=False, sheet_name='rule-count-11-to-20')
        df6.to_excel(writer, index=False, sheet_name='rules-greater-than-20')
        df7.to_excel(writer, index=False, sheet_name='other-rules')