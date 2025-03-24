import requests

BASE = "http://127.0.0.1:5000"

try:
    with open(".token", "r") as f:
        token = f.read().strip()
except FileNotFoundError:
    print(".token file not found")
    exit()

headers = {"Authorization": f"Bearer {token}"}

res = requests.get(f"{BASE}/tasks", headers = headers)

if res.status_code == 200:
    print("Tasks: ")
    for task in res.json():
        print("-", task["title"], "id:", task["id"], "user_id:", task.get("user_id"))
else:
    print("code different than 200: ", res.status_code)
    print(res.json())

