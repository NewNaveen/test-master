import requests
from requests.auth import HTTPBasicAuth
from concurrent.futures import ThreadPoolExecutor
import json
import time

header = {"Content-type": "application/json", "Accept": "application/json", "X-Allow-Overwrite": "true"}

list1 = []

for i in range(2101, 3201):
    data = {
        "transport_zone_id": "cf3bc7c9-a8cd-493b-b9e2-aa59f7453ad4",
        "replication_mode": "SOURCE",
        "admin_state": "UP",
        "display_name": f"rajuna-test-{i}",
        "hybrid": False
    }
    list1.append(data)

#  we can use basic authentication to pass the credentials

def create_ls(ls):
    url1 = "https://nsxManager.sddc-44-226-7-47.vmwarevmc.com/api/v1/logical-switches/"
    # When passing the data as json we have to dump data as JSON using json.dumps(data)
    x = requests.post(url=url1, auth=HTTPBasicAuth("admin", "Kq!PD7B!uqX5bmM"), data=json.dumps(ls), headers=header)
    time.sleep(2)
    y = x.json()
    print(y)


with ThreadPoolExecutor(max_workers=15) as e:
    e.map(create_ls, list1)