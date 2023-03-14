import os
import yaml
from yaml.loader import SafeLoader
import pandas as pd

all_files = os.listdir()

class GetAllScripts:

    def get_all_yaml_file(self, all_files):
        all_yaml_files = []
        for i in all_files:
            if i.endswith(".yaml"):
                all_yaml_files.append(i)
        return all_yaml_files

    def ro_rw_files(self, all_yaml_files):
        ro_yaml_files = []
        rw_yaml_files = []
        for j in all_yaml_files:
            with open(j) as f:
                data = yaml.load(f, Loader=SafeLoader)
                for k in data["tags"]:
                    if k["value"] == "nsx:ro":
                        ro_yaml_files.append(j)
                    elif k["value"] == "nsx:rw":
                        rw_yaml_files.append(j)
                    else:
                        continue
                f.close()
        return ro_yaml_files, rw_yaml_files

    def final_dictionary(self, all_files):
        ro_scripts = []
        rw_scripts = []
        all_yaml_files = self.get_all_yaml_file(all_files)
        ro_files, rw_files = self.ro_rw_files(all_yaml_files)

        for file in ro_files:
            with open(file) as f1:
                data = yaml.load(f1, Loader=SafeLoader)
                name = data["name"]
                description = data["description"]
                for h in data["tags"]:
                    if h["name"] == "author":
                        ro_scripts.append({"script_name": name,
                                           "script_author": h["value"],
                                           "description": description})

        for file in rw_files:
            with open(file) as f1:
                data = yaml.load(f1, Loader=SafeLoader)
                name = data["name"]
                description = data.get("description")
                for h in data["tags"]:
                    if h["name"] == "author":
                        rw_scripts.append({"script_name": name,
                                           "script_author": h["value"],
                                           "description": description})

        ro_scripts = sorted(ro_scripts, key=lambda x: x['script_author'])
        rw_scripts = sorted(rw_scripts, key=lambda x: x['script_author'])
        return ro_scripts, rw_scripts


if _name_ == '_main_':
    x = GetAllScripts()
    ro, rw = x.final_dictionary(all_files)
    df1 = pd.DataFrame.from_dict(ro)
    df2 = pd.DataFrame.from_dict(rw)
    with pd.ExcelWriter("output.xlsx") as writer:
        df1.to_excel(writer, index=False, sheet_name="RO-Scripts", engine='xlsxwriter')
        df2.to_excel(writer, index=False, sheet_name="RW-Scripts", engine='xlsxwriter')
