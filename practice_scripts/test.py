list1 = []

for i in range(201, 1101):
    data = {
        "transport_zone_id": "cf3bc7c9-a8cd-493b-b9e2-aa59f7453ad4",
        "replication_mode": "SOURCE",
        "admin_state": "UP",
        "display_name": f"rajuna-test-{i}",
        "hybrid": False
    }
    list1.append(data)

print(len(list1))
print(list1)
